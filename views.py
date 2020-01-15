"""
Gendered pronoun experiment
"""
import random
import json
import csv
import secrets

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

from gender.models import Participant
from gender.data import COUNTRIES, LANGUAGES, STATES

# Constants

PRONOUNS = [["She", "Her"], ["He", "His"], ["They", "Their"]]
TREATMENTS = ["neutral", "female", "male"]
PRONOUN_TREATMENT_COMBINATIONS = [
    ["neutral", ["She", "Her"]],
    ["neutral", ["He", "His"]],
    ["neutral", ["They", "Their"]],
    ["female", ["She", "Her"]],
    ["female", ["They", "Their"]],
    ["male", ["He", "His"]],
    ["male", ["They", "Their"]]
]

AGREE_SCALE = ["Strongly disagree", "Somewhat disagree",
               "Neither agree nor disagree", "Somewhat agree",
               "Strongly agree"]

POSITIVITY_SCALE = ["Very unfavorable", "Unfavorable",
                    "Somewhat unfavorable",
                    "Neither unfavorable nor favorable",
                    "Somewhat favorable", "Favorable", "Very favorable"]

"""
Helper functions
----------------
Generic functions which are used in various views
"""


def generic(request, key, db_id):
    """Helper function to return data from JSON given some key"""
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    data = data[key]
    context = {'questions': data, 'db_id': db_id}

    return render(request, f'gender/{key}.html', context)


def store_data(request, key):
    db_id = request.POST['db_id']
    p = Participant.objects.get(id=db_id)
    for k, v in request.POST.items():
        if k not in ["csrfmiddlewaretoken", "db_id"]:
            setattr(p, k, v)
            print(k, v)
    setattr(p, key + "_complete", timezone.now())
    p.save()
    return db_id


def is_admin(user):
    return user.is_superuser


"""
View Functions
---------
These functions take HTTP requests and return formatted HTML responses
to the user
"""


def home(request):
    """Initial page of the site"""
    # Get IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Create new data entry
    key = secrets.token_hex(16)
    p = Participant(ip_address=ip, start_time=timezone.now(), key=key)
    p.save()

    return render(request, 'gender/welcome.html', {'db_id': p.id})


def consent(request):
    """Shows the consent form"""

    # Retrieve participant db record
    db_id = store_data(request, 'welcome')

    context = {'db_id': db_id}

    return render(request, 'gender/consent.html', context)


def instructions(request):
    """Shows the instructions"""

    # Retrieve participant db record
    db_id = store_data(request, 'consent')

    context = {'db_id': db_id}

    return render(request, 'gender/instructions.html', context)


def treatment(request):
    """Shows the candidate the intervention stimulus"""

    # Retrieve participant db record
    db_id = store_data(request, 'instructions')
    p = Participant.objects.get(id=db_id)

    # randomly select condition
    # pronouns = random.choice(PRONOUNS)
    # treatment_stimulus = random.choice(TREATMENTS)
    treatment_stimulus, pronouns = random.choice(PRONOUN_TREATMENT_COMBINATIONS)

    context = {'pronouns': pronouns, "treatment": treatment_stimulus,
               'db_id': p.id}

    return render(request, 'gender/treatment.html', context)


def mediator(request):
    """Assess likelihood to imagine a nonmale"""
    db_id = store_data(request, 'treatment')
    return render(request, 'gender/mediator.html', {"db_id": db_id})


def leaders(request):
    """Assess accessibility of female politicians"""
    db_id = store_data(request, 'mediator')
    return generic(request, "leaders", db_id)


def proposals(request):
    """Assess profemale attitudes"""
    db_id = store_data(request, 'leaders')
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    context = {'questions': data["proposals"], 'db_id': db_id}
    context['options'] = AGREE_SCALE
    return render(request, f'gender/proposals.html', context)


def lgbt(request):
    """Assess positivity toward the LGBT community"""
    db_id = store_data(request, 'proposals')
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    context = {'questions': data["lgbt"], 'db_id': db_id}
    context['options'] = POSITIVITY_SCALE
    return render(request, f'gender/lgbt.html', context)


def lgbt_social(request):
    """Assess percieved social acceptibility of LGBT community"""
    db_id = store_data(request, 'lgbt')
    return generic(request, "lgbt_social", db_id)


def qualifier(request):
    """Check that candidate qualifies for the experiment"""
    db_id = store_data(request, 'lgbt_social')

    context = {"db_id": db_id, 'countries': COUNTRIES,
               'languages': LANGUAGES}
    return render(request, 'gender/qualifier.html', context)


def demographics(request):
    """Questions about candidate demographics"""
    db_id = store_data(request, 'qualifier')
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    data = data['demographics']
    context = {'questions': data, "db_id": db_id, "states": STATES}
    return render(request, 'gender/demographics.html', context)


def post_test(request):
    """Post test questionnaire to check participant's understanding
    of the experiment"""
    db_id = store_data(request, 'demographics')
    participant = Participant.objects.get(id=db_id)
    gender = participant.treatment_gender
    context = {'db_id': db_id, 'gender': gender}
    return render(request, 'gender/post_test.html', context)


def finish(request):
    """End of experiment"""
    db_id = store_data(request, 'feedback')
    p = Participant.objects.get(id=db_id)
    context = {'key': p.key}
    return render(request, "gender/finish.html", context)


@user_passes_test(is_admin)
def data(request):
    """Return a csv of participant data"""
    fields = Participant._meta.fields
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    row = [field.name for field in fields]
    writer.writerow(row)
    for obj in Participant.objects.all():
        row = [getattr(obj, field.name) for field in fields]
        writer.writerow(row)

    return response

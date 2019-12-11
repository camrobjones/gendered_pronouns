"""
Gendered pronoun experiment
"""
import random
import json

from django.shortcuts import render

# Constants

PRONOUNS = [["She", "Her"], ["He", "His"], ["They", "Their"]]
TREATMENTS = ["0", "1", "2"]

AGREE_SCALE = ["Strongly disagree", "Somewhat disagree",
               "Neither agree nor disagree", "Somewhat agree",
               "Strongly agree"]

POSITIVITY_SCALE = ["Very unfavorable", "Unfavorable",
                    "Somewhat unfavorable",
                    "Neither unfavorable nor favorable",
                    "Somewhat favorable", "Favorable", "Very favorable"]

"""
View Functions
---------
These functions take HTTP requests and return formatted HTML responses
to the user
"""


def home(request):
    """Homepage of the site"""
    return treatment(request)


def generic(request, key):
    """Helper function to return data from JSON given some key"""
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    data = data[key]
    return render(request, f'gender/{key}.html', {'questions': data})


def treatment(request):
    """Shows the candidate the intervention stimulus"""

    # randomly select condition
    pronouns = random.choice(PRONOUNS)
    treatment_stimulus = random.choice(TREATMENTS)

    context = {'pronouns': pronouns, "treatment": treatment_stimulus}

    return render(request, 'gender/treatment.html', context)


def mediator(request):
    """Assess likelihood to imagine a nonmale"""
    return render(request, 'gender/mediator.html', {})


def female_politicians(request):
    """Assess accessibility of female politicians"""
    return generic(request, "female_politicians")


def profemale(request):
    """Assess profemale attitudes"""
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    context = {'questions': data["profemale"]}
    context['options'] = AGREE_SCALE
    return render(request, f'gender/profemale.html', context)


def lgbt(request):
    """Assess positivity toward the LGBT community"""
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    context = {'questions': data["lgbt"]}
    context['options'] = POSITIVITY_SCALE
    return render(request, f'gender/lgbt.html', context)


def lgbt_social(request):
    """Assess percieved social acceptibility of LGBT community"""
    return generic(request, "lgbt_social")


def qualifier(request):
    """Check that candidate qualifies for the experiment"""
    return generic(request, "qualifier")


def demographics(request):
    """Questions about candidate demographics"""
    with open('gender/static/gender/stimuli.json') as f:
        data = json.load(f)

    data = data['demographics']
    return render(request, 'gender/demographics.html', {'questions': data})


def finish(request):
    """End of experiment"""
    return render(request, "gender/finish.html")

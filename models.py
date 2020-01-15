"""Model to store experimental data"""

from django.db import models


class Participant(models.Model):
    """Class to store participant data"""
    ip_address = models.TextField()
    key = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)

    welcome_complete = models.DateTimeField(null=True, blank=True)
    consent_complete = models.DateTimeField(null=True, blank=True)
    instructions_complete = models.DateTimeField(null=True, blank=True)

    treatment_gender = models.TextField()
    treatment_pronoun = models.TextField()
    treatment_1 = models.TextField()
    treatment_2 = models.TextField()
    treatment_3 = models.TextField()
    treatment_complete = models.DateTimeField(null=True, blank=True)

    mediator_story = models.TextField()
    mediator_complete = models.DateTimeField(null=True, blank=True)

    leaders_1 = models.TextField()
    leaders_2 = models.TextField()
    leaders_3 = models.TextField()
    leaders_4 = models.TextField()
    leaders_5 = models.TextField()
    leaders_6 = models.TextField()
    leaders_complete = models.DateTimeField(null=True, blank=True)

    proposals_1 = models.TextField()
    proposals_2 = models.TextField()
    proposals_3 = models.TextField()
    proposals_4 = models.TextField()
    proposals_5 = models.TextField()
    proposals_6 = models.TextField()
    proposals_7 = models.TextField()
    proposals_8 = models.TextField()
    proposals_complete = models.DateTimeField(null=True, blank=True)

    lgbt_1 = models.TextField()
    lgbt_2 = models.TextField()
    lgbt_complete = models.DateTimeField(null=True, blank=True)

    lgbt_social_1 = models.TextField(default="")
    lgbt_social_2 = models.TextField(default="")
    lgbt_social_3 = models.TextField(default="")
    lgbt_social_4 = models.TextField(default="")
    lgbt_social_complete = models.DateTimeField(null=True, blank=True)

    country_1 = models.TextField(default="")
    country_from_1 = models.TextField(default="")
    country_to_1 = models.TextField(default="")
    country_2 = models.TextField(default="")
    country_from_2 = models.TextField(default="")
    country_to_2 = models.TextField(default="")
    country_3 = models.TextField(default="")
    country_from_3 = models.TextField(default="")
    country_to_3 = models.TextField(default="")
    country_4 = models.TextField(default="")
    country_from_4 = models.TextField(default="")
    country_to_4 = models.TextField(default="")
    country_5 = models.TextField(default="")
    country_from_5 = models.TextField(default="")
    country_to_5 = models.TextField(default="")

    mother_country = models.TextField(default="")
    father_country = models.TextField(default="")

    language_1 = models.TextField(default="")
    language_proficiency_1 = models.TextField(default="")
    language_2 = models.TextField(default="")
    language_proficiency_2 = models.TextField(default="")
    language_3 = models.TextField(default="")
    language_proficiency_3 = models.TextField(default="")
    language_4 = models.TextField(default="")
    language_proficiency_4 = models.TextField(default="")
    language_5 = models.TextField(default="")
    language_proficiency_5 = models.TextField(default="")
    qualifier_complete = models.DateTimeField(null=True, blank=True)

    demographics_year = models.TextField(default="")
    demographics_state = models.TextField(default="")
    demographics_zip = models.TextField(default="")
    demographics_education = models.TextField(default="")
    demographics_politics = models.TextField(default="")
    demographics_gender = models.TextField(default="")
    demographics_complete = models.DateTimeField(null=True, blank=True)

    recall_1 = models.TextField(default="")
    recall_2 = models.TextField(default="")
    recall_3 = models.TextField(default="")
    feedback_1 = models.TextField(default="")
    feedback_2 = models.TextField(default="")
    feedback_complete = models.DateTimeField(null=True, blank=True)



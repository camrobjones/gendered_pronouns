"""Model to store experimental data"""

from django.db import models


class Participant(models.Model):
    """Class to store participant data"""
    ip_address = models.TextField()
    key = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)

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

    lgbt_social_1 = models.TextField()
    lgbt_social_2 = models.TextField()
    lgbt_social_complete = models.DateTimeField(null=True, blank=True)

    qualifier_1 = models.TextField()
    qualifier_2 = models.TextField()
    qualifier_3 = models.TextField()
    qualifier_complete = models.DateTimeField(null=True, blank=True)

    demographics_1 = models.TextField()
    demographics_2 = models.TextField()
    demographics_3 = models.TextField()
    demographics_4 = models.TextField()
    demographics_complete = models.DateTimeField(null=True, blank=True)



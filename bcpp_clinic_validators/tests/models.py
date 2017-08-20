from django.db import models
from edc_base.model_mixins import BaseUuidModel


class SubjectEligibility(BaseUuidModel):

    screening_identifier = models.CharField(max_length=25)

    subject_identifier = models.CharField(max_length=25)


class SubjectConsent(BaseUuidModel):

    screening_identifier = models.CharField(max_length=25)

    subject_identifier = models.CharField(max_length=25)

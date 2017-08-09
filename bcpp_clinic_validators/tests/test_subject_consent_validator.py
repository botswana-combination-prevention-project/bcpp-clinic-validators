from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..form_validators import SubjectConsentFormValidator
from .models import SubjectConsent, SubjectEligibility

from pprint import pprint


class TestFormValidator(TestCase):

    SubjectConsentFormValidator.eligibility_model = 'bcpp_clinic_validators.subjecteligibility'

    def test_validator_ok(self):
        SubjectEligibility.objects.create(screening_identifier='S12345')
        cleaned_data = dict(screening_identifier='S12345')
        form_validator = SubjectConsentFormValidator(
            cleaned_data=cleaned_data, instance=SubjectConsent())
        try:
            form_validator.validate()
        except forms.ValidationError:
            self.fail('ValidationError unexpectedly raised')
        pprint(form_validator._errors)

    def test_validator_missing_eligibility(self):
        cleaned_data = {}
        form_validator = SubjectConsentFormValidator(
            cleaned_data=cleaned_data, instance=SubjectConsent())
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('__all__', form_validator._errors)
        self.assertIn('missing_eligibility', form_validator._error_codes)

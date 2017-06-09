from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validators import EligibilityFormValidator


class TestClinicEligibilityFormValidator(TestCase):

    def test_has_identity_yes1(self):
        cleaned_data = {'has_identity': YES, 'identity': None}
        form_validator = EligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('identity'))

    def test_has_identity_yes2(self):
        cleaned_data = {'has_identity': YES, 'identity': 21222221222}
        form_validator = EligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNone(form_validator._errors.get('identity'))

    def test_has_identity_no(self):
        cleaned_data = {'has_identity': NO, 'has_identity': 21222221222}
        form_validator = EligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('identity'))

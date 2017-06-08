from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

from ..form_validators import EligibilityFormValidator


class TestClinicEligibilityFormValidator(TestCase):

    def setUp(self):
        pass

    def test_clinic_eligibility_has_identity(self):
        """Test if has_identity is Yes identity is required.
        """
        cleaned_data = {'has_identity': YES, 'identity': 2222212}
        form = EligibilityFormValidator(cleaned_data=cleaned_data)
        try:
            form.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got {e}')

    def test_clinic_eligibility_has_no_identity(self):
        """Test if has_identity is Yes identity is required.
        """
        cleaned_data = {'has_identity': YES, 'identity': None}
        form = EligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import YES

from ..validators import ClinicEligibilityFormValidator


class TestClinicEligibilityFormValidator(TestCase):

    def setUp(self):
        pass

    def test_clinic_eligibility_has_identity(self):
        """Test if has_identity is Yes identity is required.
        """
        cleaned_data = {'has_identity': YES, 'identity': 2222212}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

    def test_clinic_eligibility_has_no_identity(self):
        """Test if has_identity is Yes identity is required.
        """
        cleaned_data = {'has_identity': YES, 'identity': None}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_clinic_eligibility_has_name(self):
        """Test if first_name is Yes first_name is required.
        """
        cleaned_data = {'first_name': YES, 'first_name': 'qwerty'}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

    def test_clinic_eligibility_has_no_name(self):
        """Test if first_name is Yes first_name is required.
        """
        cleaned_data = {'first_name': YES, 'first_name': None}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_clinic_eligibility_has_initials(self):
        """Test if initials is Yes initials is required.
        """
        cleaned_data = {'initials': YES, 'initials': 'AQ'}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

    def test_clinic_eligibility_has_no_initials(self):
        """Test if has_initials is Yes initials is required.
        """
        cleaned_data = {'initials': YES, 'initials': None}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_clinic_eligibility_has_report_datetime(self):
        """Test if report_datetime is Yes report_datetime is required.
        """
        cleaned_data = {'report_datetime': YES, 'report_datetime':
                        get_utcnow()}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

    def test_clinic_eligibility_has_no_report_datetime(self):
        """Test if report_datetime is Yes report_datetime is required.
        """
        cleaned_data = {'report_datetime': YES, 'report_datetime': None}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

    def test_clinic_eligibility_has_age_in_years(self):
        """Test if age_in_years is Yes age_in_years is required.
        """
        cleaned_data = {'age_in_years': YES, 'age_in_years': '23'}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

    def test_clinic_eligibility_has_gender(self):
        """Test if gender is Yes gender is required.
        """
        cleaned_data = {'gender': YES, 'gender': 'male'}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form.clean())

    def test_clinic_eligibility_has_no_gender(self):
        """Test if gender is Yes gender is required.
        """
        cleaned_data = {'gender': YES, 'gender': None}
        form = ClinicEligibilityFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form.clean)

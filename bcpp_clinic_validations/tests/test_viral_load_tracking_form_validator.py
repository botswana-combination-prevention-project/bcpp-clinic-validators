from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO

from ..form_validators import ViralLoadTrackingFormValidator
from pprint import pprint


class TestViralLoadTrackingFormValidator(TestCase):

    def test_if_drawn_datetime_required(self):
        cleaned_data = {
            'is_drawn': YES,
            'drawn_datetime': None,
            'clinician_initials': 'XX'}
        form_validator = ViralLoadTrackingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('drawn_datetime'))

    def test_if_not_drawn_datetime_not_required1(self):
        cleaned_data = {
            'is_drawn': NO,
            'drawn_datetime': None,
            'clinician_initials': None}
        form_validator = ViralLoadTrackingFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('drawn_datetime'))
        self.assertIsNone(form_validator._errors.get('clinician_initials'))

    def test_if_not_drawn_datetime_not_required2(self):
        """Asserts raises and raises on clinician_initials, first.
        """
        cleaned_data = {'is_drawn': NO,
                        'drawn_datetime': get_utcnow(),
                        'clinician_initials': 'XX'}
        form_validator = ViralLoadTrackingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('clinician_initials'))

    def test_if_not_drawn_datetime_not_required3(self):
        """Asserts raises and raises on drawn_datetime, second.
        """
        cleaned_data = {'is_drawn': NO,
                        'drawn_datetime': get_utcnow(),
                        'clinician_initials': None}
        form_validator = ViralLoadTrackingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('drawn_datetime'))

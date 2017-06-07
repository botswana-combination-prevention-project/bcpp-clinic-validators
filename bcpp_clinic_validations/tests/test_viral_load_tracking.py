from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..validations import ViralLoadTracking
from edc_base.utils import get_utcnow


class TestViralLoadTracking(TestCase):

    def test_is_drawn_yes(self):
        cleaned_data = {'is_drawn': YES}
        form_validator = ViralLoadTracking(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_is_drawn_no(self):
        cleaned_data = {'is_drawn': NO,
                        'clinician_initials': "XX"}
        form_validator = ViralLoadTracking(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_is_drawn_datetime_yes(self):
        cleaned_data = {'is_drawn': YES}
        form_validator = ViralLoadTracking(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_is_drawn_datetime_no(self):
        cleaned_data = {'is_drawn': NO,
                        'drawn_datetime': get_utcnow()}
        form_validator = ViralLoadTracking(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

from ..validations import ViralLoadTracking
from edc_base.utils import get_utcnow


class TestViralLoadTracking(TestCase):

    def setUp(self):
        pass

    def test_is_drawn(self):
        """Test if is_drawn is Yes clinician_initials is required.
        """
        cleaned_data = {'is_drawn': YES, 'clinician_initials': None}
        viralloadtracking = ViralLoadTracking(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, viralloadtracking.clean)

    def test_is_drawn_datetime(self):
        """Test if is_drawn is Yes drawn_datetime is required.
        """
        cleaned_data = {'is_drawn': YES, 'drawn_datetime': None}
        viralloadtracking = ViralLoadTracking(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, viralloadtracking.clean)

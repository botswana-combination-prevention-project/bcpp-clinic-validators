from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from ..form_validators import SubjectVisitFormValidator


class TestFormValidator(TestCase):

    def test_(self):
        cleaned_data = {}
        form_validator = SubjectVisitFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('appointment', form_validator._errors)

from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validators import QuestionnaireFormValidator


class TestQuestionnaireFormValidator(TestCase):

    def test_knows_last_cd4_yes(self):
        cleaned_data = {'knows_last_cd4': YES}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_knows_last_cd4_no(self):
        cleaned_data = {'knows_last_cd4': NO,
                        'cd4_count': 500}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_knows_last_cd4_true(self):
        cleaned_data = {
            'knows_last_cd4': YES,
            'cd4_count': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

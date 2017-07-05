from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from edc_constants.constants import YES, NO, DWTA, NEG

from ..form_validators import QuestionnaireFormValidator
from bcpp_clinic_validations import form_validators


class TestQuestionnaireFormValidator(TestCase):
    def test_know_hiv_status_yes(self):
        cleaned_data = {'know_hiv_status': YES,
                        'current_hiv_status': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('current_hiv_status'))

    def test_know_hiv_status_dwta(self):
        cleaned_data = {'know_hiv_status': DWTA,
                        'current_hiv_status': 'NEGATIVE'}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('current_hiv_status'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_know_hiv_status_no(self):
        cleaned_data = {'know_hiv_status': NO,
                        'current_hiv_status': 'NEGATIVE'}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('current_hiv_status'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_on_arv_yes(self):
        cleaned_data = {'on_arv': YES,
                        'arv_evidence': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('arv_evidence'))

    def test_knows_last_cd4_yes1(self):
        cleaned_data = {'knows_last_cd4': YES, 'cd4_count': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('cd4_count'))

    def test_knows_last_cd4_yes2(self):
        cleaned_data = {'knows_last_cd4': YES, 'cd4_count': 500}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('cd4_count'))

    def test_knows_last_cd4_no(self):
        cleaned_data = {'knows_last_cd4': NO, 'cd4_count': 500}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('cd4_count'))

    def test_current_hiv_status_neg(self):
        cleaned_data = {'current_hiv_status': NEG,
                        'arv_evidence': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('arv_evidence'))

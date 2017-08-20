from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO, DWTA, NEG, POS, NOT_APPLICABLE

from ..form_validators import QuestionnaireFormValidator


class TestFormValidator(TestCase):

    def test_know_hiv_status_yes(self):
        cleaned_data = {'know_hiv_status': YES,
                        'current_hiv_status': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('current_hiv_status', form_validator._errors)

    def test_know_hiv_status_no(self):
        cleaned_data = {'know_hiv_status': NO,
                        'current_hiv_status': NEG}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('current_hiv_status', form_validator._errors)

    def test_on_arv_yes(self):
        cleaned_data = {'on_arv': YES,
                        'arv_evidence': NOT_APPLICABLE}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('arv_evidence', form_validator._errors)

    def test_knows_last_cd4_yes1(self):
        cleaned_data = {'knows_last_cd4': YES, 'cd4_count': None}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cd4_count', form_validator._errors)

    def test_knows_last_cd4_yes2(self):
        cleaned_data = {'knows_last_cd4': YES, 'cd4_count': 500}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError:
            self.fail('ValidationError unexpectedly raised.')
        self.assertNotIn('cd4_count', form_validator._errors)

    def test_knows_last_cd4_no(self):
        cleaned_data = {'knows_last_cd4': NO, 'cd4_count': 500}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cd4_count', form_validator._errors)

    def test_knows_last_cd4_dwta(self):
        cleaned_data = {'knows_last_cd4': DWTA, 'cd4_count': 500}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cd4_count', form_validator._errors)

    def test_arv_evidence(self):
        cleaned_data = {'know_hiv_status': YES,
                        'current_hiv_status': POS,
                        'on_arv': NO,
                        'arv_evidence': YES}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('arv_evidence', form_validator._errors)

    def test_yes_on_arvs_applicable_evidence(self):
        cleaned_data = {'on_arv': YES,
                        'arv_evidence': NO}
        form_validator = QuestionnaireFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError:
            self.fail('ValidationError unexpectedly raised.')

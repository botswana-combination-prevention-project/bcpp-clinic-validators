from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES

from ..validations import Questionnaire


class TestQuestionnaire(TestCase):

    def setUp(self):
        pass

    def test_knows_last_cd4_n_cd4_count1(self):
        """Test if knows_last_cd4 is Yes cd4_count is required.
        """
        cleaned_data = {'knows_last_cd4': YES, 'cd4_count': 390}
        questionnaire = Questionnaire(cleaned_data=cleaned_data)
        self.assertTrue(questionnaire.clean())

    def test_knows_last_cd4_n_cd4_count2(self):
        """Test if knows_last_cd4 is Yes cd4_count is required.
        """
        cleaned_data = {'knows_last_cd4': YES, 'cd4_count': None}
        questionnaire = Questionnaire(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, questionnaire.clean)

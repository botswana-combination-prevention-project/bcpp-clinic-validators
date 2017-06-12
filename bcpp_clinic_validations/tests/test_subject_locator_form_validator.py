from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validators import SubjectLocatorFormValidator


class TestSubjectLocatorFormValidator(TestCase):

    def test_home_visit_permission_yes(self):
        cleaned_data = {
            'home_visit_permission': YES,
            'physical_address': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('physical_address'))

    def test_home_visit_permission_no(self):
        cleaned_data = {'home_visit_permission': NO,
                        'physical_address': "Village"}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('physical_address'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_call_work_place_and_phone_yes(self):
        cleaned_data = {
            'may_call_work': YES,
            'subject_work_place': None,
            'subject_work_phone': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(
            form_validator._errors.get('subject_work_place',
                                       'subject_work_phone'))

    def test_may_call_work_place_no(self):
        cleaned_data = {'may_call_work': NO,
                        'subject_work_place': 'bhp'}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('subject_work_place'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_call_work_phone_no(self):
        cleaned_data = {'may_call_work': NO,
                        'subject_work_phone': 1234123}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('subject_work_phone'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_follow_up_no(self):
        cleaned_data = {'may_follow_up': NO,
                        'subject_cell': 123456}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('subject_cell'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_follow_up_yes(self):
        cleaned_data = {
            'may_follow_up': YES,
            'subject_cell': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('subject_cell'))

    def test_has_alt_contact_name_yes(self):
        cleaned_data = {'has_alt_contact': YES,
                        'alt_contact_name': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('alt_contact_name'))

    def test_has_alt_contact_name_no(self):
        cleaned_data = {'has_alt_contact': NO,
                        'alt_contact_name': "Kwasi"}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('alt_contact_name'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_has_alt_contact_rel_yes(self):
        cleaned_data = {'has_alt_contact': YES,
                        'alt_contact_name': 'Tumie',
                        'alt_contact_rel': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('alt_contact_rel'))

    def test_has_alt_contact_rel_no(self):
        cleaned_data = {'has_alt_contact': NO,
                        'alt_contact_rel': "brother"}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('alt_contact_rel'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_yes(self):
        cleaned_data = {'may_contact_someone': YES,
                        'contact_name': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('contact_name'))

    def test_may_contact_someone_name_no(self):
        cleaned_data = {'may_contact_someone': NO,
                        'contact_name': "AB"}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('contact_name'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_rel_yes(self):
        cleaned_data = {'may_contact_someone': YES,
                        'contact_name': 'AB',
                        'contact_rel': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(form_validator._errors.get('contact_rel'))

    def test_may_contact_someone_rel_no(self):
        cleaned_data = {'may_contact_someone': NO,
                        'contact_rel': 'brother'}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('contact_rel'))
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_address_yes(self):
        cleaned_data = {'may_contact_someone': YES,
                        'contact_name': 'AB',
                        'contact_rel': 'brother',
                        'contact_physical_address': None}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIsNotNone(
            form_validator._errors.get('contact_physical_address'))

    def test_may_contact_someone_address_no(self):
        cleaned_data = {'may_contact_someone': NO,
                        'contact_physical_address': "Village"}
        form_validator = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertIsNone(
            form_validator._errors.get('contact_physical_address'))
        self.assertRaises(ValidationError, form_validator.clean)

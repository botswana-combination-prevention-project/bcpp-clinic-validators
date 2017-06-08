from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validators import ClinicSubjectLocatorFormValidator


class TestClinicSubjectLocatorFormValidator(TestCase):

    def test_home_visit_permission_yes(self):
        cleaned_data = {'home_visit_permission': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_home_visit_permission_no(self):
        cleaned_data = {'home_visit_permission': NO,
                        'physical_address': "Village"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_home_visit_permission_true(self):
        cleaned_data = {
            'home_visit_permission': YES,
            'physical_address': "Village"}
        form_validator = ClinicSubjectLocatorFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form_validator.clean())

    def test_may_call_work_place_yes(self):
        cleaned_data = {'may_call_work': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_call_work_place_no(self):
        cleaned_data = {'may_call_work': NO,
                        'subject_work_place': "bhp"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_call_work_phone_yes(self):
        cleaned_data = {'may_call_work': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_call_work_phone_no(self):
        cleaned_data = {'may_call_work': NO,
                        'subject_work_phone': 123456}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_call_work_place_and_phone_true(self):
        cleaned_data = {
            'may_call_work': YES,
            'subject_work_place': "bhp",
            'subject_work_phone': 123456}
        form_validator = ClinicSubjectLocatorFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form_validator.clean())

    def test_may_follow_up_yes(self):
        cleaned_data = {'may_follow_up': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_follow_up_no(self):
        cleaned_data = {'may_follow_up': NO,
                        'subject_cell': 123456}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_follow_up_no_true(self):
        cleaned_data = {
            'may_follow_up': YES,
            'subject_cell': 123456}
        form_validator = ClinicSubjectLocatorFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form_validator.clean())

    def test_has_alt_contact_name_yes(self):
        cleaned_data = {'has_alt_contact': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_has_alt_contact_name_no(self):
        cleaned_data = {'has_alt_contact': NO,
                        'alt_contact_name': "Kwasi"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_has_alt_contact_rel_yes(self):
        cleaned_data = {'has_alt_contact': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_has_alt_contact_rel_no(self):
        cleaned_data = {'has_alt_contact': NO,
                        'alt_contact_rel': "brother"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_has_alt_contact_name_true(self):
        cleaned_data = {
            'has_alt_contact': YES,
            'alt_contact_name': "Kwasi",
            'alt_contact_rel': "brother"}
        form_validator = ClinicSubjectLocatorFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form_validator.clean())

    def test_may_contact_someone_yes(self):
        cleaned_data = {'may_contact_someone': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_name_no(self):
        cleaned_data = {'may_contact_someone': NO,
                        'contact_name': "AB"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_rel_yes(self):
        cleaned_data = {'may_contact_someone': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_rel_no(self):
        cleaned_data = {'may_contact_someone': NO,
                        'contact_rel': "brother"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_address_yes(self):
        cleaned_data = {'may_contact_someone': YES}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_address_no(self):
        cleaned_data = {'may_contact_someone': NO,
                        'contact_physical_address': "Village"}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_may_contact_someone_true(self):
        cleaned_data = {
            'may_contact_someone': YES,
            'contact_name': "AB",
            'contact_rel': "brother",
            'contact_physical_address': "Village"}
        form_validator = ClinicSubjectLocatorFormValidator(cleaned_data=cleaned_data)
        self.assertTrue(form_validator.clean())

    def test_may_sms_follow_up_not_required(self):
        cleaned_data = {
            'may_follow_up': NO,
            'may_sms_follow_up': None}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got {e}')

    def test_may_sms_follow_up_not_required_error(self):
        options = {
            'may_follow_up': NO,
            'may_sms_follow_up': YES}
        form = ClinicSubjectLocatorFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

    def test_next_of_kin_not_required(self):
        cleaned_data = {
            'next_of_kin': NO,
            'has_alt_contact': None}
        form_validator = ClinicSubjectLocatorFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got {e}')

    def test_next_of_kin_not_required_error(self):
        options = {
            'next_of_kin': NO,
            'has_alt_contact': YES}
        form = ClinicSubjectLocatorFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form.clean)

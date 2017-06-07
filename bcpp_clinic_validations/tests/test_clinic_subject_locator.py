from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..validations import ClinicSubjectLocator


class TestClinicSubjectLocator(TestCase):

    def setUp(self):
        pass

    def test_home_visit_permission(self):
        """Test if home_visit_permission is Yes physical_address is required.
        """
        cleaned_data = {'home_visit_permission': YES, 'physical_address': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_call_work_place(self):
        """Test if may_call_work is Yes subject_work_place is required.
        """
        cleaned_data = {'may_call_work': YES, 'subject_work_place': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_call_work_phone(self):
        """Test if may_call_work is Yes subject_work_phone is required.
        """
        cleaned_data = {'may_call_work': YES, 'subject_work_phone': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_follow_up_cell(self):
        """Test if subject_cell is Yes subject_cell is required.
        """
        cleaned_data = {'may_follow_up': YES, 'subject_cell': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_has_alt_contact(self):
        """Test if has_alt_contact is Yes alt_contact_name is required.
        """
        cleaned_data = {'has_alt_contact': YES, 'alt_contact_name': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_has_alt_contact_rel(self):
        """Test if has_alt_contact is Yes alt_contact_rel is required.
        """
        cleaned_data = {'has_alt_contact': YES, 'alt_contact_rel': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_contact_someone_name(self):
        """Test if may_contact_someone is Yes contact_name is required.
        """
        cleaned_data = {'may_contact_someone': YES, 'contact_name': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_contact_someone_rel(self):
        """Test if may_contact_someone is Yes contact_rel is required.
        """
        cleaned_data = {'may_contact_someone': YES, 'contact_rel': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_contact_someone_address(self):
        """Test if may_contact_someone is Yes contact_physical_address is
        required.
        """
        cleaned_data = {'may_contact_someone': YES,
                        'contact_physical_address': None}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_may_follow_up(self):
        """If participant has not given permission for follow-up, do not give
        follow-up details
        """
        cleaned_data = {'may_follow_up': NO,
                        'may_sms_follow_up': 123456}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

    def test_next_of_kin(self):
        """If participant has not given permission to contact next_of_kin,
        do not give next_of_kin details
        """
        cleaned_data = {'next_of_kin': NO,
                        'has_alt_contact': YES}
        clinicsubjectlocator = ClinicSubjectLocator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, clinicsubjectlocator.clean)

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO


class ClinicSubjectLocatorFormValidator(FormValidator):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='home_visit_permission',
            field_required='physical_address',
        )
        self.required_if(
            YES,
            field='may_call_work',
            field_required='subject_work_place',
        )
        self.required_if(
            YES,
            field='may_call_work',
            field_required='subject_work_phone',
        )
        self.required_if(
            YES,
            field='may_follow_up',
            field_required='subject_cell',
        )
        self.required_if(
            YES,
            field='has_alt_contact',
            field_required='alt_contact_name',
        )
        self.required_if(
            YES,
            field='has_alt_contact',
            field_required='alt_contact_rel',
        )
        self.required_if(
            YES,
            field='may_contact_someone',
            field_required='contact_name',
        )
        self.required_if(
            YES,
            field='may_contact_someone',
            field_required='contact_rel',
        )
        self.required_if(
            YES,
            field='may_contact_someone',
            field_required='contact_physical_address',
        )
        self.not_required_if(
            NO,
            field='may_follow_up',
            field_required='may_sms_follow_up',
        )
        self.not_required_if(
            NO,
            field='next_of_kin',
            field_required='has_alt_contact',
        )
        return self.cleaned_data

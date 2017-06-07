from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class ClinicSubjectLocator(FormValidator):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='home_visit_permission',
            field_required='physical_address',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='may_call_work',
            field_required='subject_work_place',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='may_call_work',
            field_required='subject_work_phone',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='may_follow_up',
            field_required='subject_cell',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='has_alt_contact',
            field_required='alt_contact_name',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='has_alt_contact',
            field_required='alt_contact_rel',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='may_contact_someone',
            field_required='contact_name',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='may_contact_someone',
            field_required='contact_rel',
            cleaned_data=self.cleaned_data)
        self.required_if(
            YES,
            field='may_contact_someone',
            field_required='contact_physical_address',
            cleaned_data=self.cleaned_data)
        self.not_required_if(
            NO,
            field='may_follow_up',
            field_required='may_sms_follow_up',
            cleaned_data=self.cleaned_data)
        self.not_required_if(
            NO,
            field='next_of_kin',
            field_required='has_alt_contact',
            cleaned_data=self.cleaned_data)
        return self.cleaned_data

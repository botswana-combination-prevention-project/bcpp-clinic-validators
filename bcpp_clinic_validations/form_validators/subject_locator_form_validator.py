from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class SubjectLocatorFormValidator(FormValidator):

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
#      return self.cleaned_data

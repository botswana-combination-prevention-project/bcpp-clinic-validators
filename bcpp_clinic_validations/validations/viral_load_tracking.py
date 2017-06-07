from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class ViralLoadTracking(FormValidator):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='is_drawn',
            field_required='clinician_initials',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='is_drawn',
            field_required='drawn_datetime',
            cleaned_data=self.cleaned_data)
        return self.cleaned_data

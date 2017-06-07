from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class ViralLoadTrackingFormValidator(FormValidator):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='is_drawn',
            field_required='clinician_initials')

        self.required_if(
            YES,
            field='is_drawn',
            field_required='drawn_datetime')
        return self.cleaned_data

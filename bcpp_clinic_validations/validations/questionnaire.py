from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class Questionnaire(FormValidator):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='knows_last_cd4',
            field_required='cd4_count',
            cleaned_data=self.cleaned_data)

        return self.cleaned_data

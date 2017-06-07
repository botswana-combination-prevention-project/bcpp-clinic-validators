from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, NO, UNKNOWN


class QuestionnaireFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='knows_last_cd4',
            field_required='cd4_count')

        return self.cleaned_data

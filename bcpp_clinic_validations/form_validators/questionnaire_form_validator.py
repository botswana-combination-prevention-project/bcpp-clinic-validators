from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, DWTA, NEG, UNKNOWN


class QuestionnaireFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='know_hiv_status',
            field_required='current_hiv_status')

        self.not_required_if(
            DWTA,
            field='know_hiv_status',
            field_required='current_hiv_status')

        self.not_applicable_if(
            UNKNOWN,
            field='know_hiv_status',
            field_required='current_hiv_status')

        self.required_if(
            YES,
            field='on_arv',
            field_required='arv_evidence')

        self.required_if(
            YES,
            field='knows_last_cd4',
            field_required='cd4_count')

        self.not_applicable_if(
            NEG,
            field='current_hiv_status',
            field_applicable='arv_evidence')
#        return self.cleaned_data

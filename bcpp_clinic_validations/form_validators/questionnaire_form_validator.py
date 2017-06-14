from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, DWTA


class QuestionnaireFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='know_hiv_status',
            field_required='current_hiv_status')

        self.not_required_if(
            DWTA,
            field='know_hiv_status',
            field_required='current_hiv_status'
        )

        self.required_if(
            YES,
            field='on_arv',
            field_required='arv_evidence')

        self.required_if(
            YES,
            field='knows_last_cd4',
            field_required='cd4_count')

#        return self.cleaned_data

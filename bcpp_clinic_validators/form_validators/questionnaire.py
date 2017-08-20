from django import forms

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, POS


class QuestionnaireFormValidator(FormValidator):

    def clean(self):

        self.applicable_if(
            YES, field='know_hiv_status', field_applicable='current_hiv_status')

        if self.cleaned_data.get('know_hiv_status') == YES:
            if (self.cleaned_data.get('current_hiv_status')) not in [POS]:
                raise forms.ValidationError(
                    {'current_hiv_status': 'PPT is not eligible if not '
                     'HIV Positive, Please check eligibility checklist'})

        self.applicable_if(
            YES, field='on_arv', field_applicable='arv_evidence')

        self.required_if(
            YES,
            field='knows_last_cd4',
            field_required='cd4_count')

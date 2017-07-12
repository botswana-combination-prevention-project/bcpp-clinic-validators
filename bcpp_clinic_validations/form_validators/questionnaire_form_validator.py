from django import forms

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, DWTA, NO, POS


class QuestionnaireFormValidator(FormValidator):

    def clean(self):
        cleaned_data = super().clean()
        self.validate_hiv_status()
        self.currently_taking_ARVS()
        return cleaned_data

    def validate_hiv_status(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('know_hiv_status') == NO:
            raise forms.ValidationError(
                {'know_hiv_status':
                    'Please Check Eligibility Checklist for HIV Results.'}
            )

        elif cleaned_data.get('know_hiv_status') == YES:
            if (cleaned_data.get('current_hiv_status')) not in [POS]:
                raise forms.ValidationError(
                    {'current_hiv_status': 'PPT is not Eligible if not '
                     'HIV Positive, Please Check eligibiliy Checklist'}
                )

        return cleaned_data

    def currently_taking_ARVS(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('on_arv') == NO:
            if cleaned_data.get('arv_evidence') in [DWTA, NO, YES]:
                raise forms.ValidationError(
                    'PPT cannot have ARV evidence when not on ARV')

        elif cleaned_data.get('on_arv') == YES:
            if cleaned_data.get('arv_evidence') not in [NO, YES]:
                raise forms.ValidationError(
                    'PPT has to specify ARV Evidence since PPT is on ARV')

        self.required_if(
            YES,
            field='knows_last_cd4',
            field_required='cd4_count')

        return cleaned_data

from django import forms
from edc_constants.constants import YES, DWTA, NEG, NO, POS

from edc_base.modelform_validators import FormValidator


class QuestionnaireFormValidator(FormValidator):

    def clean(self):
        cleaned_data = super().clean()
        self.validate_hiv_status()
        self.currently_taking_ARVS()
        return cleaned_data

    def validate_hiv_status(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('know_hiv_status') == NO:
            if cleaned_data.get('current_hiv_status') in [POS, NEG]:
                raise forms.ValidationError(
                    'PPT does not know HIV Status Expecting Unknown')

            if cleaned_data.get('on_arv') in [DWTA, NO, YES]:
                raise forms.ValidationError(
                    'PPT cannot take ARV while HIV status is Unknown')

        elif cleaned_data.get('know_hiv_status') == YES:
            if cleaned_data.get('current_hiv_status') not in [POS, NEG]:
                raise forms.ValidationError(
                    'PPT has to specify the HIV result since known status is YES')

            if (cleaned_data.get('current_hiv_status') == NEG and
                    cleaned_data.get('on_arv') == YES):
                raise forms.ValidationError(
                    'PPT cannot be on ART while HIV NEGATIVE')

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

        self.not_required_if(
            NO,
            field='knows_last_cd4',
            field_required='cd4_count')

        return cleaned_data

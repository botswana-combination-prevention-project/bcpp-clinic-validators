from edc_base.modelform_mixins import RequiredFieldValidationMixin
from edc_constants.constants import YES, NO, UNKNOWN


class ClinicEligibilityForm(RequiredFieldValidationMixin):
    
    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='has_identity',
            field_required='identity',
            cleaned_data=self.cleaned_data)

        return self.cleaned_data
    
    def clean(self):
        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='first_name' ,
            cleaned_data=self.cleaned_data)

        return self.cleaned_data
    
        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='initials' ,
            cleaned_data=self.cleaned_data)

        return self.cleaned_data
    
        self.required_if(
            YES,
            field='clinic_household_member',
            field_required= 'report_datetime' ,
            cleaned_data=self.cleaned_data)

        return self.cleaned_data
    
        self.required_if(
            YES,
            field='clinic_household_member',
            field_required= 'age_in_years',
            cleaned_data=self.cleaned_data)

        return self.cleaned_data
    
        self.required_if(
            YES,
            field='clinic_household_member',
            field_required= 'gender',
            cleaned_data=self.cleaned_data)

    
    
    
        
    
    

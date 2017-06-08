from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class ClinicEligibilityFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='has_identity',
            field_required='identity',
        )

        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='first_name',
        )

        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='initials',
        )

        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='report_datetime',
        )

        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='age_in_years',
        )

        self.required_if(
            YES,
            field='clinic_household_member',
            field_required='gender',
        )

        return self.cleaned_data

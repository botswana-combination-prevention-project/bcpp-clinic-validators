from django import forms

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, DWTA, NO, POS


class SubjectEligibilityFormValidator(FormValidator):

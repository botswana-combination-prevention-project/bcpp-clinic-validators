from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_base.modelform_validators import FormValidator


class SubjectConsentFormValidator(FormValidator):

    eligibility_model = 'bcpp_clinic_subject.subjecteligibility'

    @property
    def eligibility_model_cls(self):
        return django_apps.get_model(self.eligibility_model)

    def clean(self):
        if not self.instance.id:
            try:
                self.eligibility_model_cls.objects.get(
                    screening_identifier=self.cleaned_data.get('screening_identifier'))
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    'Complete the eligibility checklist first.',
                    code='missing_eligibility')

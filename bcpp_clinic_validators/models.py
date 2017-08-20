from django.conf import settings

if settings.APP_NAME == 'bcpp_clinic_validators':
    from .tests import models

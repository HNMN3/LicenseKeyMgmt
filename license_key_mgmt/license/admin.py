from django.contrib import admin
from .models import LicenseKeyModel


class LicenseAdmin(admin.ModelAdmin):
    exclude = ('license_hw_id',)


# Register your models here.
admin.site.register(LicenseKeyModel, LicenseAdmin)

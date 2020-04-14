from django.db import models
from uuid import uuid4, getnode


def generate_license_key():
    return str(uuid4()).upper()


# Create your models here.
class LicenseKeyModel(models.Model):
    class Meta:
        verbose_name = 'LicenseKey'
        verbose_name_plural = 'License Keys'

    license_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    license_key = models.CharField(max_length=100, default=generate_license_key)
    license_hw_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.license_key

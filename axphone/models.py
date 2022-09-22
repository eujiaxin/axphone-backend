
from django.db import models
# from phonenumber_filed.modelfields import PhoneNumberField
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}:{self.phone_number}'

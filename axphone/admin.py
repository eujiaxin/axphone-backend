from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list = ('name', 'phone_number')


admin.site.register(Contact, ContactAdmin)

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Customer

class CustomerModelAdmin(ModelAdmin):
    model = Customer
    list_display = (
        'username',
        'email',
        #'phone_number',
        'age',
        'address',
        'active',
        'customer_code',
    )

admin.site.register(Customer, CustomerModelAdmin)

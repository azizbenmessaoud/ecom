from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User

# customer
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=300, unique=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    
    # problem 2 : dont know why phone number field is not displaying a widget on the admin side
    
    # phone_number = PhoneNumberField(region="RO")
    
    age = models.IntegerField(default=18, blank=True)
    address = models.CharField(max_length=300, default='no street', blank=True)
    active = models.BooleanField(default=False)

    # problem 1 : when creating the funtion generate_customer_code, it s impossible to reference 
    #             the Customer model within itself in order to get ensure a unique ccustomer_code for 
    #             every Customer instance

    # def generate_user_code():
    #     from secrets import token_hex
    #     code = token_hex(5)
    #     while super().get_queryset().filter(customer_code=code).count() != 0:
    #         code = token_hex(5)

    customer_code = models.CharField(max_length=300, default='hei', unique=True) # default=generate_customer_code()

    def __str__(self):
        return self.username  


    

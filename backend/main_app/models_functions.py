
def generate_user_code():
    from secrets import token_hex
    code = token_hex(5)
    from .models import Customer
    while Customer.objects.filter(customer_code=code).count() != 0:
        code = token_hex(5) 
    return code
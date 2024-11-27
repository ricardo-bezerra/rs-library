from django.db import models

# Customer table
class Customer(models.Model):

    customer_id = models.UUIDField(primary_key=True, editable=False)
    customer_name = models.CharField(max_length=25)
    customer_surname = models.CharField(max_length=55)
    customer_location = models.CharField(max_length=25)
    employee_zipcode = models.CharField(max_length=25)
    employee_birth = models.DateField(blank=True, default="") 
    customer_address =  models.CharField(max_length=150)
    customer_job_type = models.CharField(max_length=35)
    customer_create_at = models.DateField(auto_now_add=True)

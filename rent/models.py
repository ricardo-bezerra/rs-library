from django.db import models

# Rent table
class Rent(models.Model):
    rent_id = models.AutoField(primary_key=True, editable=False)
    rent_date = models.DateField(blank=True, default="")
    rent_invoice = models.CharField(max_length=25)
    rent_product = models.CharField(max_length=55)
    rent_amount_product = models.FloatField()
    rent_payment_method = models.IntegerField() # Payment method table
    rent_condition = models.IntegerField() # Condition payment method table - total | installments
    rent_descount = models.FloatField()
    rent_taxes = models.FloatField()
    rent_employee_commission = models.FloatField(blank=True, default="")
    rent_start_date = models.DateField(blank=True, default="")
    rent_end_date = models.DateField(blank=True, default="")
    book_id = models.IntegerField()
    employee_id = models.IntegerField()
    customer_id = models.IntegerField()
    condition_id = models.IntegerField()
    payment_method_id = models.IntegerField()

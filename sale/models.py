from django.db import models

# Sale table
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True, editable=False)
    sale_date = models.DateField(blank=True, default="")
    sale_invoice = models.CharField(max_length=25)
    sale_product = models.CharField(max_length=55)
    sale_amount_product = models.FloatField()
    sale_payment_method = models.IntegerField() # Payment method table
    sale_condition = models.IntegerField() # Condition payment method table - total | installments
    sale_descount = models.FloatField()
    sale_taxes = models.FloatField()
    employee_id = models.IntegerField()
    book_id = models.IntegerField()
    customer_id = models.IntegerField()
    condition_id = models.IntegerField()
    payment_method_id = models.IntegerField() 
    sale_employee_commission = models.FloatField(blank=True, default="")


# Condition payment method table
class Condition(models.Model):
    condition_id = models.AutoField(primary_key=True, editable=False)
    condition_description = models.CharField(max_length=25) # total | installments
    sale_id = models.IntegerField()


# Payment method table
class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True, editable=False)
    payment_method_description = models.CharField(max_length=55) # credit card | debit card | money | library club card

from django.db import models

# from uuid import uuid4


# Department table
class Department(models.Model):
    department_id = models.AutoField(primary_key=True, editable=False)
    department_name = models.CharField(max_length=55)


# Employee lambda function load picture in table field
def upload_employee_image(instance, filename):
   return f"{instance.employee_id}, {filename}"

# Employee table
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True, editable=False)
    employee_name = models.CharField(max_length=55)
    employee_access_code = models.CharField(max_length=25)
    employee_document = models.IntegerField()
    employee_gender = models.IntegerField() # 1- Male | 2- Female
    employee_address = models.CharField(max_length=100)
    employee_zipcode = models.CharField(max_length=25)
    employee_birth = models.DateField(blank=True, default="")
    employee_parents = models.CharField(max_length=55)
    employee_born_place = models.CharField(max_length=55)
    employee_start_date = models.DateField(blank=True, default="")
    employee_department = models.IntegerField() # Fk table Department
    employee_function = models.IntegerField() # Fk table Function
    employee_salary = models.FloatField()
    employee_marital_status = models.IntegerField() # Fk table Marital Status
    employee_photo = models.ImageField()

    department_id = models.IntegerField()
    function_id = models.IntegerField()
    marital_status_id = models.IntegerField()

    employee_image = models.ImageField(upload_to=upload_employee_image, blank=True, null=True)


# Function (at work) table
class Function(models.Model):
    function_id = models.AutoField(primary_key=True, editable=False)
    function_name = models.CharField(max_length=55)


# Marital Status table
class MaritalStatus(models.Model):
    marital_status_id = models.AutoField(primary_key=True, editable=False)
    marital_status_description = models.CharField(max_length=23) # Single | Married | Widower | Divorced | Separate


# Book lambda function load picture in table field
def upload_book_image(instance, filename):
   return f"{instance.book_id}, {filename}"

# Book table
class Book(models.Model):

    book_id = models.AutoField(primary_key=True, editable=False)
    book_title = models.CharField(max_length=55)
    book_author = models.CharField(max_length=55)
    book_release_year = models.DateField()
    book_state = models.CharField(max_length=15)
    book_pages = models.IntegerField()
    book_publishing_company = models.CharField(max_length=55)
    book_create_at = models.DateField(auto_now_add=True)

    book_image = models.ImageField(upload_to=upload_book_image, blank=True, null=True)


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


# Book storage lambda function load picture in table field
def upload_book_storage_image(instance, filename):
   return f"{instance.book_id}, {filename}"

# Book storage table
class BookStorage(models.Model):

    book_storage_id = models.AutoField(primary_key=True, editable=False)
    book_storage_title = models.CharField(max_length=55)
    book_storage_author = models.CharField(max_length=55)
    book_storage_release_year = models.DateField()
    book_storage_state = models.CharField(max_length=15)
    book_storage_pages = models.IntegerField()
    book_storage_publishing_company = models.CharField(max_length=55)
    book_storage_create_at = models.DateField(auto_now_add=True)
    book_storage_quantity = models.IntegerField()
    book_id = models.IntegerField()

    book_storage_image = models.ImageField(upload_to=upload_book_storage_image, blank=True, null=True)


# Payment method table
class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True, editable=False)
    payment_method_description = models.CharField(max_length=55) # credit card | debit card | money | library club card
    

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

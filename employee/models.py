from django.db import models

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
    marital_status_description = models.CharField(max_length=23) # Single | Married | Widower | Divorced | Separated

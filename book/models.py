from django.db import models

# from uuid import uuid4


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
    
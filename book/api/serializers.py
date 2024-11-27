from rest_framework import serializers
from book.models import Book, BookStorage


class BookSerializer(serializers.ModelSerializer):

    class Meta:
       
        model = Book
       
        fields = ('book_title', 
                  'book_author', 
                  'book_release_year', 
                  'book_state', 
                  'book_pages', 
                  'book_publishing_company', 
                  'book_image')

        # fields = '__all__'

class BookStorageSerializer(serializers.ModelSerializer):
     
    class Meta:
       
        model = BookStorage
       
        fields = ('book_storage_id', 
                  'book_storage_title', 
                  'book_storage_author', 
                  'book_storage_release_year', 
                  'book_storage_state', 
                  'book_storage_pages', 
                  'book_storage_publishing_company', 
                  'book_storage_create_at', 
                  'book_storage_quantity', 
                  'book_id', 
                  'book_storage_image')

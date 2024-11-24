from rest_framework import serializers
from book.models import Book,Employee,MaritalStatus,PaymentMethod,Department,Function,Customer,BookStorage,Sale,Condition,Rent


class BookSerializer(serializers.ModelSerializer):

    class Meta:
       
        model = Book
       
        fields = ('book_title',
                  'book_author',
                  'book_release_year',
                  'book_state',
                  'book_pages',
                  'book_publishing_company',
                  'book_create_at',
                  'book_image')

        # fields = '__all__'

from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from book.models import *

from book.api.serializers import *

from django.http.response import JsonResponse

@csrf_exempt
def bookApi(request, id=0):
    if request.method=='GET':
        book = Book.objects.all()
        book_serializer = BookSerializer(Book, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    elif request.method=='POST':
        book_data = JsonResponse().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Process realized with success!", safe=False)
        return JsonResponse("Process not realized!", safe=False)

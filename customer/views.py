from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from customer.models import Customer

from customer.api.serializers import CustomerSerializer, serializers

from django.http.response import JsonResponse

@csrf_exempt
def customerApi(request, id=0):
    if request.method=='GET':
        customer = Customer.objects.all()
        customer_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
    """
    elif request.method=='POST':
        book_data = JSONParser().parse(request)
        book = Book.objects.get(book_id=book_data["book_id"])
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Process realized with success!", safe=False)
        return JsonResponse("Process not realized!", safe=False)
    
    elif request.method=='PUT':
        book_data = JSONParser().parse(request)
        book = Book.objects.get(book_id=book_data["book_id"])
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Process actualized with success!", safe=False)
        return JsonResponse("Process not actualized!", safe=False)

    elif request.method=='DELETE':
        book = Book.objects.get(book_id=id)
        book.delete()
        return JsonResponse("Book deleted with success!", safe=False)
"""
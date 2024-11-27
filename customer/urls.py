from django.urls import re_path as url
from customer import views


urlpatterns = [
    url(r'^customer/$', views.customerApi),
    url(r'^customer/([0-9]+)$', views.customerApi),
]
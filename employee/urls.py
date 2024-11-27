from django.urls import re_path as url
from employee import views


urlpatterns = [
    url(r'^employee/$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),
]
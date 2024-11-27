from django.urls import re_path as url
from sale import views


urlpatterns = [
    url(r'^sale/$', views.saleApi),
    url(r'^sale/([0-9]+)$', views.saleApi),
]
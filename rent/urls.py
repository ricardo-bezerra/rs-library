from django.urls import re_path as url
from rent import views


urlpatterns = [
    url(r'^rent/$', views.rentApi),
    url(r'^rent/([0-9]+)$', views.rentApi),
]
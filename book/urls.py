from django.urls import re_path as url
from book import views


urlpatterns = [
    url(r'^book/$', views.bookApi),
    url(r'^book/([0-9]+)$', views.bookApi),
]

# url(r'book/', views.bookApi),

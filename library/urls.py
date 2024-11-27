from rest_framework import routers

from book.api import viewsets as bookviewsets

from django.conf.urls.static import static

from django.conf import settings

from django.contrib import admin

from django.urls import path, include, re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('book.urls')),
    url(r'^', include('customer.urls')),
    url(r'^', include('employee.urls')),
    url(r'^', include('rent.urls')),
    url(r'^', include('sale.urls'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from newsapps.views import home
from django.contrib import admin
from django.urls import path
from newsapps.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home)
]

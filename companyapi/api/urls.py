from django.contrib import admin
from django.urls import path, include
from api.views import Companyviewset, Employeeviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', Companyviewset)
router.register(r'employees', Employeeviewset)

urlpatterns = [
    path('', include(router.urls))
]

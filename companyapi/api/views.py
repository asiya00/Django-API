from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

# Create your views here.
class Companyviewset(viewsets.ModelViewSet):
	queryset=Company.objects.all()
	serializer_class=CompanySerializer 

	@action(detail=True, methods=['get'])
	def employee(self, request,pk=None):
		company = Company.objects.get(pk=pk)
		employees = Employee.objects.filter(Company_id=company)
		emps_serializer = EmployeeSerializer(employees, many=True, context={'request':request})
		return Response(emps_serializer.data)


class Employeeviewset(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
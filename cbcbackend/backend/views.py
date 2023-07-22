from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from backend.models import Data,Studentreg,Course,Branch,Reference,Billingdata
from backend.serializers import DataSerializer, StudentregSerializer,CourseSerializer,BranchSerializer,ReferenceSerializer,BillingSerializer
from rest_framework.parsers import MultiPartParser

# Create your views here.


class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.AllowAny]  
    
class StudentregView(viewsets.ModelViewSet):
    queryset = Studentreg.objects.all()
    serializer_class = StudentregSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['student_id','batch','branch','course','status']

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]  

class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.AllowAny]  

class ReferenceView(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.AllowAny]

class BillingView(viewsets.ModelViewSet):
    queryset = Billingdata.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['student_id',]

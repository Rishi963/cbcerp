from django.contrib.auth.models import User
from backend.models import Data,Studentreg,Course,Branch,Reference,Billingdata
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields='__all__'
class StudentregSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studentreg
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billingdata
        fields = '__all__'
        
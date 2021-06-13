from rest_framework import serializers 
from management.models import Students
from datetime import date
 
 
class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Students
        fields = "__all__"


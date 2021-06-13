from rest_framework import serializers 
from management.models import Students
from datetime import date
 
 
class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Students
        fields = "__all__"

    def validate_age(self, dob):  
        if dob <= 18:  
            raise serializers.ValidationError(('%(age) should be more than 18'), 
            params= {'age':dob},)



from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view ,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated


@swagger_auto_schema(methods=['post'], request_body=StudentSerializer)
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def management_list(request):
    
    if request.method == 'GET':
        """ Get all students data """
        students = Students.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            students = students.filter(title__icontains=name)
        
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
        
       
    elif request.method == 'POST':
        """ Post New student data """
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    elif request.method == 'DELETE':
        """ Delete all students data """
        count = Students.objects.all().delete()
        return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@swagger_auto_schema(methods=['put'], request_body=StudentSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def management_detail(request, pk):
    """ using try catch to avoid app crashing"""
    try:
        student = Students.objects.get(pk=pk)
        if request.method == 'GET': 
            """ Get students data by id"""
            student_serializer = StudentSerializer(student) 
            return JsonResponse(student_serializer.data)

        elif request.method == 'PUT': 
            """ Edit students data by id"""
            student_data = JSONParser().parse(request) 
            student_serializer = StudentSerializer(student, data=student_data) 
            if student_serializer.is_valid(): 
                student_serializer.save() 
                return JsonResponse(student_serializer.data) 
            return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            """ Delete students data by id"""
            student.delete() 
            return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Students.DoesNotExist: 
        """ if Find Nay issues Throw error with status code 404 """
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND) 


def dashboard(request):
    """Function to visit the dashboard """
    return render(request, 'dashboard.html')
        
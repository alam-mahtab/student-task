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

test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)

user_response = openapi.Response('response description', StudentSerializer)

# # 'method' can be used to customize a single HTTP method of a view
# @swagger_auto_schema(method='get', manual_parameters=[test_param], responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=StudentSerializer)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def management_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        students = Students.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            students = students.filter(title__icontains=name)
        
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Students.objects.all().delete()
        return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@swagger_auto_schema(methods=['put'], request_body=StudentSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def management_detail(request, pk):
    # find tutorial by pk (id)
    try:
        student = Students.objects.get(pk=pk)
        if request.method == 'GET': 
            student_serializer = StudentSerializer(student) 
            return JsonResponse(student_serializer.data)

        elif request.method == 'PUT': 
            student_data = JSONParser().parse(request) 
            student_serializer = StudentSerializer(student, data=student_data) 
            if student_serializer.is_valid(): 
                student_serializer.save() 
                return JsonResponse(student_serializer.data) 
            return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            student.delete() 
            return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    # try: 
    #     management = Students.objects.get(pk=pk) 
    except Students.DoesNotExist: 
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
def homepage(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
        
# @api_view(['GET'])
# def management_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
from django.urls import path
from management import views 

 
urlpatterns = [ 
    path('api/dashboard',views.dashboard), # url to visit the dashboard
    path('api/management', views.management_list), # url for posting new data and getting or delete all data
    path('api/management/<int:pk>', views.management_detail), # url for getting deleting and editing data by id
]
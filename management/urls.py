from django.urls import path
from management import views 

 
urlpatterns = [ 
    path('api/home',views.homepage),
    path('api/dashboard',views.dashboard),
    path('api/management', views.management_list),
    path('api/management/<int:pk>', views.management_detail),
    #url(r'^api/managment/published$', views.tutorial_list_published)
]
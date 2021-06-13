"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include, re_path
# from django.views.generic import TemplateView
# from rest_framework.schemas import get_schema_view

# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mahtab API",
        default_version='v1',
        description="Welcome to the world of Mahtab",
        #terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="alammahtab869@gmail.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    permission_classes=(permissions.AllowAny,),  # If I change the permission it throws an exception. See below
    public=False,
    #patterns=public_apis,
)
# ends here

 

urlpatterns = [
    # re_path(r'^docs(?P<format>\.json|\.yaml)$',
    #         schema_view.without_ui(cache_timeout=0,), name='schema-json'),  #<-- Here
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0,),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path('admin/', admin.site.urls),
    path('', include('management.urls')),
    path('accounts/',include('accounts.urls'))
    # path('openapi', get_schema_view(
    #         title="Your Project",
    #         description="API for all things …",
    #         version="1.0.0"
    #     ), name='openapi-schema'),
]

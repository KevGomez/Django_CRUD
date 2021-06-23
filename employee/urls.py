from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'get_list', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path("", include(router.urls))
]

from django.urls import path, include
from .views import StudentApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("student", StudentApi, basename="student")

urlpatterns = [
    path("", include(router.urls)),
]

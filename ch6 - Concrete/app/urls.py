from django.urls import path
from .views import StudentLCApi, StudentRUDApi


urlpatterns = [
    path("student/", StudentLCApi.as_view()),
    path("student/<int:pk>/", StudentRUDApi.as_view()),
]

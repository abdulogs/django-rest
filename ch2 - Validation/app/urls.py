from django.urls import path
from .views import StudentApi
# from .views import studentApi

urlpatterns = [
    # path("student/<int:pk>/", studentApi, name="studentApi"),
    # path("student/", studentApi, name="studentApi"),
    # path("student/", studentApi, name="studentApi"),
    path("student/", StudentApi.as_view(), name="studentApi"),
    path("student/<int:pk>/", StudentApi.as_view(), name="studentApi"),
]

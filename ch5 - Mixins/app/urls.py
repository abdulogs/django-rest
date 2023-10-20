from django.urls import path
from .views import StudentListApi, StudentSingleApi, StudentCreateApi, StudentUpdateApi, StudentDeleteApi


urlpatterns = [
    path("student/", StudentListApi.as_view()),
    # path("student/<int:pk>/", StudentSingleApi.as_view()),
    # path("student/", StudentCreateApi.as_view()),
    # path("student/<int:pk>/", StudentUpdateApi.as_view()),
    path("student/<int:pk>/", StudentDeleteApi.as_view()),
]

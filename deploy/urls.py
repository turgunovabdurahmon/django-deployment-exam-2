from django.urls import path
from .views import StudentListCreateApiVIew, StudentDetailApiView



urlpatterns = [
    path("student/", StudentListCreateApiVIew.as_view()),
    path("student/detail/<int:pk>/", StudentDetailApiView.as_view()),
]
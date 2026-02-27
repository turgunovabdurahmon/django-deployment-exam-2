from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .serializer import StudentSerializer
# Create your views here.



class CustomPaginator(PageNumberPagination):
    page_size = 20


class StudentListCreateApiVIew(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPaginator


class StudentDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
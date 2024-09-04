from django.shortcuts import render
from .models import AboutMeModel, ResumeModel, ContactModel, CourseModel, CourseFileModel, CourseListModel, \
    ResumeListModel
from .serializers import AboutMeModelSerializer, ResumeSerializer, ContactSerializer, CourseFileSerializer, \
    CourseListSerializer, CourseSerializer, ResumeListSerializer
from rest_framework import generics, permissions


# Create your views here.

class AboutMeView(generics.ListAPIView):
    serializer_class = AboutMeModelSerializer
    queryset = AboutMeModel.objects.all()
    permission_classes = [permissions.AllowAny]


class ResumeView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ResumeModel.objects.filter(name__id_name__icontains=self.kwargs['name'])


class ResumeListView(generics.ListAPIView):
    queryset = ResumeListModel.objects.all()
    serializer_class = ResumeListSerializer
    permission_classes = [permissions.AllowAny]


class ContactView(generics.ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class CourseView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CourseModel.objects.filter(name__id_name__icontains=self.kwargs['name'])


class CourseListView(generics.ListAPIView):
    queryset = CourseListModel.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [permissions.AllowAny]


class CourseFileView(generics.ListAPIView):
    serializer_class = CourseFileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CourseFileModel.objects.filter(name__id_name__icontains=self.kwargs['name'])


class CourseFileDetailView(generics.ListAPIView):
    serializer_class = CourseFileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CourseFileModel.objects.filter(description=self.kwargs['name'])

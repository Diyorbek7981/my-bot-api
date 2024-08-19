from django.shortcuts import render
from .models import AboutMeModel, ResumeModel, ContactModel, CoursesModel, CourseFileModel
from .serializers import AboutMeModelSerializer, ResumeSerializer, ContactSerializer, KurslarSerializer, \
    CourseFileSerializer
from rest_framework import generics, permissions


# Create your views here.

class AboutMeView(generics.ListAPIView):
    serializer_class = AboutMeModelSerializer
    queryset = AboutMeModel.objects.all()
    permission_classes = [permissions.AllowAny]


class ResumeView(generics.ListAPIView):
    queryset = ResumeModel.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.AllowAny]


class ContactView(generics.ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class KurslarView(generics.ListAPIView):
    queryset = CoursesModel.objects.filter(name__icontains='About')
    serializer_class = KurslarSerializer
    permission_classes = [permissions.AllowAny]


class FoundationView(generics.ListAPIView):
    queryset = CoursesModel.objects.filter(name__icontains='Foundation')
    serializer_class = KurslarSerializer
    permission_classes = [permissions.AllowAny]


class TgBotView(generics.ListAPIView):
    queryset = CoursesModel.objects.filter(name__icontains='TgBot')
    serializer_class = KurslarSerializer
    permission_classes = [permissions.AllowAny]


class PyBackView(generics.ListAPIView):
    queryset = CoursesModel.objects.filter(name__icontains='PyBack')
    serializer_class = KurslarSerializer
    permission_classes = [permissions.AllowAny]


class MisollarView(generics.ListAPIView):
    queryset = CourseFileModel.objects.filter(name__name='Foundation')
    serializer_class = CourseFileSerializer
    permission_classes = [permissions.AllowAny]

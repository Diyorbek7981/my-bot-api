from django.shortcuts import render
from .models import AboutMeModel, ResumeModel, ContactModel
from .serializers import AboutMeModelSerializer, ResumeSerializer, ContactSerializer
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

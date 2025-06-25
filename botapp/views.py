from django.shortcuts import render
from .models import AboutMeModel, ResumeModel, ContactModel, CourseModel, CourseFileModel, CourseListModel, \
    ResumeListModel, AboutCourseModel, Users
from .serializers import AboutMeModelSerializer, ResumeSerializer, ContactSerializer, CourseFileSerializer, \
    CourseListSerializer, CourseSerializer, ResumeListSerializer, AboutCourseModelSerializer, UsersSerializer
from rest_framework import generics, permissions
from .pagination import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return CourseFileModel.objects.filter(name__id_name__icontains=self.kwargs['name'])


class CourseFileDetailView(generics.ListAPIView):
    serializer_class = CourseFileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CourseFileModel.objects.filter(description=self.kwargs['name'])


class AboutCourseView(generics.ListAPIView):
    queryset = AboutCourseModel.objects.all()
    serializer_class = AboutCourseModelSerializer
    permission_classes = [permissions.AllowAny]


class UsersView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


class CreateUserView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


class UserGetView(APIView):
    def get(self, request, telegram_id, format=None):
        try:
            user = Users.objects.filter(telegram_id=telegram_id).first()
        except Users.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the user data and return it in the response
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

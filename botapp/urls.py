from django.urls import path
from .views import AboutMeView, ResumeView, ContactView, CourseView, CourseListView, ResumeListView, CourseFileView, \
    CourseFileDetailView

urlpatterns = [
    path('about/', AboutMeView.as_view(), name='about'),
    path('resume/<str:name>', ResumeView.as_view(), name='resume'),
    path('resume_list/', ResumeListView.as_view(), name='resume_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('course_list/', CourseListView.as_view(), name='course_list'),
    path('course/<str:name>', CourseView.as_view(), name='course'),
    path('course_file/<str:name>', CourseFileView.as_view(), name='course_file'),
    path('course_file_det/<str:name>', CourseFileDetailView.as_view(), name='course_file_detail'),
]

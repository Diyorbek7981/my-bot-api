from django.urls import path
from .views import AboutMeView, ResumeView, ContactView, KurslarView

urlpatterns = [
    path('about/', AboutMeView.as_view(), name='about'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('kurslar/', KurslarView.as_view(), name='kurslar'),
]

from django.urls import path
from .views import AboutMeView, ResumeView, ContactView, KurslarView, FoundationView, TgBotView, PyBackView, \
    MisollarView

urlpatterns = [
    path('about/', AboutMeView.as_view(), name='about'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('kurslar/', KurslarView.as_view(), name='kurslar'),
    path('foundation/', FoundationView.as_view(), name='foundation'),
    path('tgbot/', TgBotView.as_view(), name='tgbot'),
    path('pyback/', PyBackView.as_view(), name='pyback'),
    path('misollar/', MisollarView.as_view(), name='misollar'),
]

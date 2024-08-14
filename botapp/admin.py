from django.contrib import admin
from .models import AboutMeModel, ResumeModel, ContactModel, KurslarModel


# Register your models here.

@admin.register(AboutMeModel)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(KurslarModel)
class KurslarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first')
    list_display_links = ('id', 'first')

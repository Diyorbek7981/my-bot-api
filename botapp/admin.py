from django.contrib import admin
from .models import AboutMeModel, ResumeModel, ContactModel, CoursesModel, CourseFileModel


# Register your models here.

@admin.register(AboutMeModel)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')


@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(CoursesModel)
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(CourseFileModel)
class CourseFileModelModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

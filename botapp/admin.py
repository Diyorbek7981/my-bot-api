from django.contrib import admin
from .models import AboutMeModel, ResumeModel, ContactModel, CourseModel, CourseFileModel, CourseListModel, \
    ResumeListModel, ContactListModel, AboutCourseModel


# Register your models here.

@admin.register(AboutMeModel)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')


@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ResumeListModel)
class ResumeListModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_name')
    list_display_links = ('id', 'name', 'id_name')


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ContactListModel)
class ContactListModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('id', 'name', 'link')


@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(CourseListModel)
class CourseListModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_name')
    list_display_links = ('id', 'name', 'id_name')


@admin.register(CourseFileModel)
class CourseFileModelModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')


@admin.register(AboutCourseModel)
class AboutCourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

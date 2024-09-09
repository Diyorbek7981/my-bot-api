from rest_framework import serializers
from .models import AboutMeModel, ResumeModel, ContactModel, CourseModel, CourseFileModel, CourseListModel, \
    ContactListModel, AboutCourseModel


class AboutMeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeModel
        fields = ('photo', 'description')

    photo = serializers.CharField(source='photo_path')  # rasm uerlni telegramga mos qilib path ko'rinishiga o'tkazadi


class ResumeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseListModel
        fields = ('id_name', 'name')


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = ('name', 'file')

    file = serializers.CharField(source='file_path')
    name = ResumeListSerializer()


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactListModel
        fields = ('name', 'link', 'confirm')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('name', 'links')

    links = ContactListSerializer(many=True)


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseListModel
        fields = ('id_name', 'name')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ('name', 'photo', 'dec_for_course', 'during_course')

    photo = serializers.CharField(source='image_path')
    name = CourseListSerializer()


class CourseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFileModel
        fields = ('name', 'file', 'description')

    file = serializers.CharField(source='file_path')
    name = CourseListSerializer()


class AboutCourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCourseModel
        fields = ('title', 'photo', 'description')

    photo = serializers.CharField(source='image_path')

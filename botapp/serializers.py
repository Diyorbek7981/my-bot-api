from rest_framework import serializers
from .models import AboutMeModel, ResumeModel, ContactModel, CoursesModel, CourseFileModel
from rest_framework.exceptions import ValidationError


class AboutMeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeModel
        fields = ('photo', 'description')

    photo = serializers.CharField(source='photo_path')  # rasm uerlni telegramga mos qilib path ko'rinishiga o'tkazadi


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = ('name', 'cv', 'resume_eng', 'resume_ru')

    cv = serializers.CharField(source='cv_path')
    resume_eng = serializers.CharField(source='resume_eng_path')
    resume_ru = serializers.CharField(source='resume_ru_path')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'


class KurslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesModel
        fields = ('name', 'title', 'dec_1', 'photo', 'kurs_davomida')

    photo = serializers.CharField(source='image_path')


class CourseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFileModel
        fields = ('name', 'file', 'description')

    file = serializers.CharField(source='file_path')

from rest_framework import serializers
from .models import AboutMeModel, ResumeModel, ContactModel, KurslarModel


class AboutMeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeModel
        fields = '__all__'

    photo = serializers.CharField(source='photo_path')  # rasm uerlni telegramga mos qilib path ko'rinishiga o'tkazadi


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = '__all__'

    cv = serializers.CharField(source='cv_path')
    resume_eng = serializers.CharField(source='resume_eng_path')
    resume_ru = serializers.CharField(source='resume_ru_path')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'


class KurslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = KurslarModel
        fields = '__all__'

    photo = serializers.CharField(source='image_path')

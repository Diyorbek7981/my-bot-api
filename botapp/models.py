from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.


class AboutMeModel(models.Model):
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True,
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=24)
    technology = models.TextField()
    telegram = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def photo_path(self):
        return self.photo.path


class ResumeModel(models.Model):
    name = models.CharField(max_length=120)
    cv = models.FileField(upload_to='file/', null=True, blank=True)
    resume_eng = models.FileField(upload_to='file/', null=True, blank=True)
    resume_ru = models.FileField(upload_to='file/', null=True, blank=True)

    @property
    def cv_path(self):
        return self.cv.path

    @property
    def resume_eng_path(self):
        return self.resume_eng.path

    @property
    def resume_ru_path(self):
        return self.resume_ru.path

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    telegram = models.URLField()
    linktee = models.URLField()
    instagram = models.URLField(default='https://www.instagram.com/abdurakhimov_7981/')
    facebook = models.URLField()

    def __str__(self):
        return self.name

from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AboutMeModel(BaseModel):
    photo = models.ImageField(upload_to='user_photos/',
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    description = models.TextField()

    def __str__(self):
        return self.description[:30]

    @property
    def photo_path(self):
        return self.photo.path


class ResumeModel(BaseModel):
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


class ContactModel(BaseModel):
    name = models.CharField(max_length=120)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    linktee = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class CoursesModel(BaseModel):
    name = models.CharField(max_length=120, )
    title = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='kurs/',
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    dec_1 = models.TextField(null=True, blank=True)
    kurs_davomida = models.TextField(null=True, blank=True, )

    @property
    def image_path(self):
        return self.photo.path

    def __str__(self):
        return self.name


class CourseFileModel(BaseModel):
    name = models.ForeignKey(CoursesModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to='exam/', null=True, blank=True)

    def __str__(self):
        return self.name.name

    @property
    def file_path(self):
        return self.file.path

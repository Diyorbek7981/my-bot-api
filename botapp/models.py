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


class ResumeListModel(BaseModel):
    id_name = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ResumeModel(BaseModel):
    name = models.ForeignKey(ResumeListModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='file/', null=True, blank=True)

    @property
    def file_path(self):
        return self.file.path

    def __str__(self):
        return self.name.name


class ContactListModel(BaseModel):
    name = models.CharField(max_length=120)
    link = models.URLField()
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContactModel(BaseModel):
    name = models.CharField(max_length=120)
    links = models.ManyToManyField(ContactListModel)

    def __str__(self):
        return self.name


class CourseListModel(BaseModel):
    id_name = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class CourseModel(BaseModel):
    name = models.ForeignKey(CourseListModel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='kurs/',
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    dec_for_course = models.TextField(null=True, blank=True)
    during_course = models.TextField(null=True, blank=True, )

    @property
    def image_path(self):
        return self.photo.path

    def __str__(self):
        return self.name.name


class CourseFileModel(BaseModel):
    name = models.ForeignKey(CourseListModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, )
    file = models.FileField(upload_to='exam/', null=True, blank=True)

    def __str__(self):
        return self.name.name

    @property
    def file_path(self):
        return self.file.path


class AboutCourseModel(BaseModel):
    title = models.CharField(max_length=120, )
    photo = models.ImageField(upload_to='kurs/',
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def image_path(self):
        return self.photo.path

from django.db import models
from django.db.models import Model
from .validators import validate_file_extension


# Create your models here.
class UploadFileModel(Model):
    file = models.FileField(upload_to="uploads/", validators=[validate_file_extension])

    def __str__(self):
        return self.title
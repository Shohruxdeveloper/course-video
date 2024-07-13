from django.core.validators import FileExtensionValidator
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='media/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'wmv', 'png', 'jpg'])])

    def __str__(self):
        return self.title

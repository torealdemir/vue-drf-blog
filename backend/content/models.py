from django.db import models
from ckeditor.fields import RichTextField


class BlogContent(models.Model):
    title = models.CharField(max_length = 50)
    body = RichTextField()
    

from django.db import models

import os
import random

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "mashroom/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    
    blog_title = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to=upload_image_path)
    blog_description = models.TextField()

    def __str__(self):
        return self.blog_title

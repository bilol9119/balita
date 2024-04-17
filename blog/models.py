from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tags(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='post/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField()

    tags = models.ManyToManyField(Tags, null=True, blank=True)
    is_advertised = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BioPost(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='bio_post/')
    description = RichTextField()
    quote = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


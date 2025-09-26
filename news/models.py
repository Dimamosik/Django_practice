from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
 feature/photo_upload
from django.core.exceptions import ValidationError

 main

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 feature/photo_upload
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

 main
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
 feature/photo_upload
        return reverse('news_detail', kwargs={'pk': self.pk})
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_content(self):
        return self.content
    
    def set_content(self, content):
        self.content = content

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_created_at(self):
        return self.created_at
    
    def get_updated_at(self):
        return self.updated_at
    
    def clean(self):
        if not self.title or len(self.title.strip()) == 0:
            raise ValidationError({'title': "Title cannot be empty."})
        if len(self.title) > 200:
            raise ValidationError({'title': "Title cannot exceed 200 characters."})
        if not self.content or len(self.content.strip()) == 0:
            raise ValidationError({'content': "Content cannot be empty."})
        

        return reverse('news_detail', kwargs={'pk': self.pk})
 main

from django.db import models
from django.urls import reverse
from users.models import User
from .utils import get_markdown


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @property
    def rendered_content(self):
        return get_markdown(self.content)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class SiteSettings(models.Model):
    hero_image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    hero_title = models.CharField(max_length=200, default="Welcome to GameLog")
    hero_subtitle = models.TextField(default="Your gaming community hub for news, reviews, and discussions.")

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

"""
모델 Post: django.db의 models.Model을 상속받음, JPA 엔티티와 유사
- author: 
- title: 
- text: 
- created_date: 
- published_date: 
"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
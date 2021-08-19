from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscriptioni', null=False)

    class Meta: # 외부 설정 정보 저장
        unique_together = ['user', 'project']
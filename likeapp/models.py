from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record', null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record', null=False)

    class Meta:
        unique_together = ['user', 'article'] # 한 게시글에 한 유저가 되도록 하는 것 (unique 하게)
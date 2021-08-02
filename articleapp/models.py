from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # ForeignKey: 1대다로 연결해 주는 것 -> 한사람이 게시글 하나만 쓸 수 있는 것은 아니기 때문에
    # related_name: 유저와 연결되어 있는 article을 접근할 때 쓰는 이름
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    # upload_to: media 폴더 내에 article이라는 폴더를 새로 생성해 거기에 이미지 저장
    content = models.TextField(null=True)
    # TestField: 긴 텍스트를 받을 때 쓰는 것
    created_at = models.DateField(auto_now_add=True)
    # auto_now_add: 굳이 서버에 설정하거나 사용자에게 입력받지 않아도 db에 생성된 시간을 기록해 자동으로 출력하는 것
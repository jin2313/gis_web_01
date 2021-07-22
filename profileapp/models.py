from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model): # 클래스 명의 소문자 버전이 db의 이름으로 지정됨 -> 바꿀 수도 있음
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # on_delete: 연결되어 있는 유저 객체가 사라지면 얘도 삭제
    # related_name: 연결된 유저 객체에서 'profile'을 사용해서 이 모델에 접근 가능
    image = models.ImageField(upload_to='profile/', null=True) # 이미지 값을 여기에 저장
    # upload_to: 받아온 이미지를 이 경로에 저장
    nickname = models.CharField(max_length=30, unique=True)
    # unique: 고유한 값만 가능
    message = models.CharField(max_length=200, null=True)
    # null: 꼭 있어야 하는 건 아님 (있어도 되고 없어도 됨)
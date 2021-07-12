from accountapp.views import hello_world, AccountCreateView
from django.urls import path

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create') # 경로, 함수(클래스일 때 as.view() 사용), 이름
]
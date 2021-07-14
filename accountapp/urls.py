from django.contrib.auth.views import LoginView, LogoutView

from accountapp.views import hello_world, AccountCreateView
from django.urls import path

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), # 경로, 뷰, 이름 순서로 적기
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create') # 경로, 함수(클래스일 때 as.view() 사용), 이름
]
"""practice_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')), # 주소창에 이거를 치면 accounts에서 하위 분기를 한다는 뜻
    path('profiles/', include('profileapp.urls')), # 여기 적힌 url이 profileapp의 urls에 적힌 app_name을 뜻함
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')), # include: commentapp에서 하위 분기
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 개발 환경에서 이미지를 제공해 줄 수 있는 코드 (배포용에 사용하면 안 됨)
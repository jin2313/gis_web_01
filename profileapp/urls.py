from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')
    # 제일 처음에 mainapp의 url에서 update로 분기했기 때문에 각 앱 안에서 이름이 겹쳐도 괜찮
]
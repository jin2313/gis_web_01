from django.urls import path

from projectapp.views import ProjectCreateView

app_name = 'projectapp' # reverse 쓸 때 사용하는 것

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),

]
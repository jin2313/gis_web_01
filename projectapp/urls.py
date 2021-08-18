from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = 'projectapp' # reverse 쓸 때 사용하는 것

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('list/', ProjectListView.as_view(), name='list'),
]
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk}) # self.object: 현재 뷰에서 만들고 있는 객체 => project


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs): # projectapp에서 articleapp의 데이터를 사용할 수 있게끔 하는 것
        user = self.request.user
        project = self.object
        subscription = Subscription.objects.filter(user=user, project=project)
        if subscription.exists(): # 탬플릿 단에서 구독 정보가 있는지 없는지 확인하기 위한 코드
            subscription = 1
        else:
            subscription = None

        article_list = Article.objects.filter(project=self.object) # filter: 조건을 걸러내는 메소드
        return super().get_context_data(object_list=article_list, subscription=subscription, **kwargs)



class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user # 지금 요청을 보내는 유저 -> 로그인되어 있지 않을 때 실행하면 문제가 생김
        project = Project.objects.get(pk=kwargs['project_pk']) # 지금 요청하는 유저가 구독을 누른 프로젝트
        # request 요청의 kwargs 안에 있는 project_pk를 의미
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs): # 게시판 구독 후 어떤 페이지로 갈지, get_success_url을 대체하는 것
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']})


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list' # 아래 함수의 반환값
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self): # get_context_data랑 차이점: 이건 템플릿에서 사용되는 모든 문맥 데이터를 조작하는 것 -> queryset보다 큰 개념, queryset: 쓰이는 모델에 적용할 조건만 쓸 수 있음
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project') # 프로젝트 정보만 가져오는 것
        article_list = Article.objects.filter(project__in=project_list) # 프로젝트 리스트 안에 있는 게시글을 전부 가져옴
        return article_list
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article


@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    elif request.method == 'GET':
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm # 입력 폼을 뭘 쓸건지
    # success_url = reverse_lazy('accountapp:hello_world') # 클래스에서는 reverse 대신 reverse_lay 사용
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk}) # 여기서 self.object가 지칭하는 것은 target_user


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # html에서 특정 객체에 접근하는 이름 지정
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)


has_ownership = [login_required, account_ownership_required]


@method_decorator(has_ownership, 'get') # get, post는 클래스 안에 들어 있는 메소드이기 때문에 이런 형식으로 적어야 함
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountapp/delete.html'
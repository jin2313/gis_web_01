from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            temp = request.POST.get('hello_world_input')
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        elif request.method == 'GET':
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login')) # 그때 reverse가 뭐였지?



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm # 입력 폼을 뭘 쓸건지
    success_url = reverse_lazy('accountapp:hello_world') # 클래스에서는 reverse 대신 reverse_lay 사용
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # html에서 특정 객체에 접근하는 이름 지정
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:hello_world')
    context_object_name = 'target_user'
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    print('home')
    count = User.objects.count()
    return render(request,'home.html',{'count':count})
def signup(request):
    print('signup')
    if request.method == 'POST':
        print('post')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            return HttpResponse('not valid')
    else:
        print('not post')
        form = UserCreationForm()
        params = {'form':form}
        return render(request,'registration/signup.html',params)
@login_required
def secret_page(request):
    return render(request,'secret_page.html')

class SecretPage(LoginRequiredMixin,TemplateView):
    template_name = 'secret_page_2.html'
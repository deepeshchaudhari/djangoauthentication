from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
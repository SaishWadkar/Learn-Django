from django.shortcuts import render
from users.models import User
from users.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'users/index.html')

def users_list(request):

    list = User.objects.all()
    ulist = {'users_list':list}

    return render(request,'users/users.html',context=ulist)

def new_user_view(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Form is invalid !')
    return render(request,'users/signup.html',context={'form':form})

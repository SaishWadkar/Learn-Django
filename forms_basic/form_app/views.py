from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'form_app/index.html')

def user_input_form_view(request):
    form = forms.UserInputForm()
    if request.method =="POST":
        form = forms.UserInputForm(request.POST)
        if form.is_valid():
            print("Validation success")
            print("Name : ",form.cleaned_data['name'])
            print("Email : ",form.cleaned_data['email'])
            print("Text : ",form.cleaned_data['text'])

    return render(request,'form_app/form.html',context={'form':form})

from django.shortcuts import render

# Create your views here.

def index(request):

    my_dict = {"text":"Saish Wadkar , you rock !" , "number":1998}

    return render(request,'app/index.html',context=my_dict)

def other(request):
    return render(request,'app/other.html')

def relative(request):
    return render(request,'app/relative_url_templates.html')

from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'name':"my name is Rahul"}
    return render(request,'post/home.html', context)
from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':'(this is sent)',
        "var":"great"
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is services page")
def contact(request):
    return HttpResponse("This is contact page")
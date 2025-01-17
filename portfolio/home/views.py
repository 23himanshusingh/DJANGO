from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name': 'Harry', 'course' : 'Django'}
    return render(request,'home.html', context)

def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("This is my contact page (/contact)")
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name,email,phone,desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written to db")
    return render(request,'contact.html')

def projects(request):
    # return HttpResponse("This is my projects (/projects)")
    return render(request,'projects.html')
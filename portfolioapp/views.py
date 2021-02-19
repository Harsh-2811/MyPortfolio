from django.shortcuts import render,HttpResponse
from .models import Certificates,Project,Technology
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
# Create your views here.
def index(request):
    certificates = Certificates.objects.all()
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    return render(request,'index.html',{'certificates':certificates,'projects':projects,'technologies':technologies})

@csrf_exempt
def sendemail(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(name+ " want to ask/tell something " ,"Email : \n "+ email +message,'harshweb2811@gmail.com',['harshpatel281199@gmail.com'])

        msg =  json.dumps({"status":"success","data":"Sent"})
        return HttpResponse(msg)


def projectpage(request,slug):
    project = Project.objects.get(slug=slug)

    return render(request,'modal.html',{'project':project})
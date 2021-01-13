from django.shortcuts import redirect,render
from .models import Contactusform,User
from django.views.generic import View
from django.http import HttpResponse
from .forms import Contactform
from django.http import JsonResponse,HttpResponseServerError
from . import forms

# Create your views here.

def contactusform_view(request):

    # if request.method=="POST":
        # contactusform=Contactusform()
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # phone_no = request.POST.get('phone_no')
        # description=request.POST.get('description')

        # contactusform.name =  name
        # contactusform.email = email
        # contactusform.phone_no = phone_no
        # contactusform.description = description
        # contactusform.save()

    form = forms.Contactform()
    return render(request,'contactusform/form.html', {'form': form})


def database_view(request):
    form = User.objects.all()
    return render(request,'contactusform/database.html', {'form': form})

def redirect_view(request):
    response = redirect('/register')
    return response
    
def saveuser_view(request):
    if request.method!="POST":
        return HttpResponseServerError()
    if request.method=="POST":
        contactusform=User()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        description=request.POST.get('description')

        contactusform.name =  name
        contactusform.email = email
        contactusform.phone_no = phone_no
        contactusform.description = description
        contactusform.save()
        
    return JsonResponse({"response":"success"})
import re
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable1": "This is sent",
        "variable2": "This is also great"
    }

    return render(request, 'index.html', context)
    #return HttpResponse("This is a Home-Page")
 
def about(request):
    return render(request, 'about.html')

def services(request): 
    return render(request, 'services.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted successfully!')
    return render(request, 'contact.html') 
   
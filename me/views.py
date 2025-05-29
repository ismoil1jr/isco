from django.shortcuts import render
from django.core.mail import send_mail
from .models import Contact



# Create your views here.
def index(request):
    return render(request,'index.html')




def contact_view(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
    return render(request, 'contact.html')










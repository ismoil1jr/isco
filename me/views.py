from django.shortcuts import render
from .models import About, Project, VisitorInfo
import uuid


def index(request):
    about = About.objects.last()
    project = Project.objects.all()

    context = {
        'about':about,
        'project':project,
    }

    return render(request,'index.html',context)


def save_visitor_info(request):
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    VisitorInfo.objects.create(ip_address=ip, user_agent=user_agent)
    

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))






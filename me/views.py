from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import AboutMe, Project, ContactMessage
import requests


def index(request):
    about = AboutMe.objects.last()
    projects = Project.objects.all()

    context = {
        "about": about,
        "project": projects,
    }
    return render(request, "index.html", context)


def contact_submit(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Invalid request"}, status=405)

    name = request.POST.get("user_name")
    email = request.POST.get("user_email")
    message_text = request.POST.get("message")

    if not all([name, email, message_text]):
        return JsonResponse(
            {"success": False, "message": "All fields are required."},
            status=400
        )

    message = ContactMessage.objects.create(
        name=name,
        email=email,
        message=message_text
    )

    try:
        sent = send_to_telegram(message)
        if sent:
            message.is_sent_to_telegram = True
            message.save()
    except Exception as e:
        # Telegram ishlamasa ham sayt yiqilmasin
        print("Telegram error:", e)

    return JsonResponse({"success": True})


def send_to_telegram(message):
    text = (
        "📩 NEW CONTACT MESSAGE\n\n"
        f"👤 Name: {message.name}\n"
        f"📧 Email: {message.email}\n\n"
        f"💬 Message:\n{message.message}"
    )

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
    }

    response = requests.post(url, json=payload, timeout=5)
    response.raise_for_status()

    return True

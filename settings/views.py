import project
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from unit.models import *
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.


def home(request):
    settings = Settings.objects.last()
    units = Unit.objects.all()
    image = Image.objects.all()[:3]
    paginator = Paginator(units, 1)
    page = request.GET.get("page")
    page_ogj = paginator.get_page(page)
    context = {"units": page_ogj, "settings": settings, "image": image}

    return render(request, "settings/home.html", context)


def services(request):
    services = Services.objects.all()[:3]
    services_2 = Services.objects.all()[3:6]
    services_3 = Services.objects.all()[6:]
    context = {"services": services, "services_2": services_2, "services_3": services_3}
    return render(request, "settings/services.html", context)


def about_us(request):
    units = Unit.objects.all()
    context = {"units": units}

    return render(request, "settings/about_us.html", context)


@login_required
def contact(request):
    settings = Settings.objects.last()
    if request.method == "POST":
        name = request.POST["text"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        send_mail(
            subject,
            message,
            email,
            [project.settings.EMAIL_HOST_USER],
        )

        return redirect("/")

    return render(request, "settings/contact.html", {"settings": settings})

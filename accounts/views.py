from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse_lazy
from .forms import SignupForm, PasswordChangingForm
from django.contrib.auth import login
from .models import *
from unit.models import *
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required


def sign_up(request, backend="django.contrib.auth.backends.ModelBackend"):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            use = form.cleaned_data["username"]
            em = form.cleaned_data["email"]
            user = User.objects.create(username=use, email=em)
            user.set_password(form.cleaned_data["password2"])
            user.save()

            if user is not None:
                if user.is_active:
                    login(
                        request,
                        user,
                        backend="django.contrib.auth.backends.ModelBackend",
                    )

                    return redirect("/accounts/profile")
    else:
        form = SignupForm()

    return render(request, "accounts/sign_up.html", {"form": form})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def my_reservation(request):
    unit_list = UnitBook.objects.filter(user=request.user)
    if len(unit_list) > 0:
        return render(request, "accounts/reservations.html", {"unit_list": unit_list})
    else:
        make_reservation = "You don't have any reservation yet"
        return render(
            request,
            "accounts/reservations.html",
            {"make_reservation": make_reservation},
        )


def check_reservation(request, id):
    check_book = UnitBook.objects.get(id=id)
    return render(
        request, "accounts/check_reservation.html", {"check_book": check_book}
    )


def cancel_reservation(request, id):
    cancel_book = UnitBook.objects.get(id=id)
    cancel_book.delete()
    return redirect("/accounts/reservation")


def change_password(request):
    if request.method == "post":
        form = PasswordChangingForm(user=request.user)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data["new_password2"])
            user.save()
    else:
        form = PasswordChangingForm(user=request.user)

    return render(request, "registration/password_change_form.html", {"form": form})

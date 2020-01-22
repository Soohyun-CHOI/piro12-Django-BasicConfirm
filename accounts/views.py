from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from askdjango import settings


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


"""
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    ctx = {
        "form": form
    }
    return render(request, "accounts/signup.html", ctx)
"""

signup = CreateView.as_view(model=User,
                            form_class=UserCreationForm,
                            success_url=settings.LOGIN_URL,  # 다음 위치
                            template_name="accounts/signup.html")

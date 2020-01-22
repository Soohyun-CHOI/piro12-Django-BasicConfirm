from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView

from accounts.forms import SignupForm


"""
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인 처리
            auth_login(request, user)
            next_url = request.GET.get("next") or "accounts:profile"
            return redirect(next_url)
    else:
        form = SignupForm()

    ctx = {
        "form": form
    }
    return render(request, "accounts/signup.html", ctx)
"""


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "accounts/signup.html"

    def get_success_url(self):
        next_url = self.request.GET.get("next") or "accounts:profile"
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect("accounts:profile")


signup = SignupView.as_view()


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
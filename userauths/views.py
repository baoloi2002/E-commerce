from django.shortcuts import render
from userauths.forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from userauths.models import User


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegistrationForm()

    context = {"form": form}

    return render(request, "userauths/sign-up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("core:index")
        else:
            messages.warning(request, "Invalid credentials")

    context = {}
    return render(request, "userauths/sign-in.html", context)

def logout_view(request):    
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("userauths:sign-in")
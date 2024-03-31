from django.shortcuts import render
from userauths.forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate


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

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")
    return render(request, "contact.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already registered.")
            return render(request, "register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        login(request, user)
        return redirect("dashboard")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def transactions(request):
    return render(request, "transactions.html")


@login_required
def budgets(request):
    return render(request, "budgets.html")


@login_required
def goals(request):
    return render(request, "goals.html")


@login_required
def profile(request):
    return render(request, "profile.html")

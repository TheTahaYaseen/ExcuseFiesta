from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from fiesta.models import Excuse, ExcuseCategory, UserProfile

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "fiesta/home.html", context)

def feed_view(request):
    context = {}
    return render(request, "fiesta/feed.html", context)
    
def register_view(request):
    
    error = ""
    form = UserCreationForm()

    if request.method == "POST":

        profile_picture = request.POST.get("profile_picture")
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            UserProfile.objects.create(
                associated_user = user,
                profile_picture = profile_picture
            )
            login(request, user)
            return redirect("home")
        else:
            error = form.errors.as_text()
            
    context = {"error": error, "form": form}
    return render(request, "fiesta/register.html", context)
    
def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            error = "User Does Not Exist!"

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "An Error Occured During Login!"

    context = {"error": error}
    return render(request, "fiesta/login.html", context)
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("home")

def user_profile_view(request):
    context = {}
    return render(request, "fiesta/user_profile.html", context)
    
def update_user_profile_view(request):
    context = {}
    return render(request, "fiesta/update_user_profile.html", context)
    
def delete_user_profile_view(request):
    context = {}
    return render(request, "fiesta/delete_user_profile.html", context)
    
def excuses_view(request):
    context = {}
    return render(request, "fiesta/excuses.html", context)
    
def excuse_view(request):
    context = {}
    return render(request, "fiesta/excuse.html", context)
    
def excuse_categories_view(request):
    context = {}
    return render(request, "fiesta/excuse_categories.html", context)
    
def excuse_category_view(request):
    context = {}
    return render(request, "fiesta/excuse_category.html", context)

def create_excuse_view(request):
    
    error = ""
    categories = ExcuseCategory.objects.all()

    if request.method == "POST":
        excuse = request.POST.get("excuse")
        excuse_category = request.POST.get("category")
        created_by = request.user

        try:
            category = ExcuseCategory.objects.get_or_create(
                name = excuse_category
            )

        except Exception:
            error = "Something Went Wrong In Creating Excuse Category!"

        if not error:

            try:
                excuse = Excuse.objects.create(
                    excuse = excuse,
                    category = category,
                    created_by = created_by
                )

            except Exception:
                error = "Something Went Wrong In Creating Excuse!"

        if not error:
            return redirect("home")

    context = {"error": error, "categories": categories}
    return render(request, "fiesta/excuse_form.html", context)
    
def update_excuse_view(request, primary_key):

    excuse = Excuse.objects.get(id = primary_key)
    error = ""
    categories = ExcuseCategory.objects.all()

    if request.method == "POST":
        excuse.excuse = request.POST.get("excuse")
        excuse_category = request.POST.get("category")
        category = ExcuseCategory(
            name = excuse_category
        )
        excuse.category = category

    context = {"error": error, "categories": categories, "excuse": excuse}
    return render(request, "fiesta/excuse_form.html", context)
    
def delete_excuse_view(request):
    context = {}
    return render(request,
     "fiesta/delete_excuse.html", context)
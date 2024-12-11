# Django authentication libaries
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    error_message = None
    form = AuthenticationForm()
    # When user hits 'login' button, then POST request is sent is generated
    if request.method == "POST":
        # read the data sent by the form via POST request
        form = AuthenticationForm(data=request.POST)
        # check if the form is valid
        if form.is_valid():
            # get the username and password
            username = form.cleaned_data["username"]  # Read username
            password = form.cleaned_data["password"]  # Read password

            # use Django's built-in authenticate function to check if the user is valid
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("recipes:list")  # send user to the desired page
        else:
            error_message = "Oops! Something went wrong."  # error message
    context = {"form": form, "error_message": error_message}
    return render(request, "auth/login.html", context)


def logout_view(request):
    logout(request)  # use Django's built-in logout function
    return redirect("login")  # after logout, send user to login page

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAccountForm
# for flashing messages
from django.contrib import messages
from .models import Account

# Create your views here.
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'accounts/index.html')


def registerAccount(request):
    # check for session in cookie to check if already logged in
    if request.user.is_authenticated:
        return redirect('index')
    # to render login n register in same page using variable 'page'
    page = 'register'
    # importing custom form with name n email n stuff
    form = CustomAccountForm()
    context = {'page': page, 'form': form}
    # creating instance of the form with 'POST' data
    if request.method == 'POST':
        form = CustomAccountForm(request.POST)
        email = request.POST['email']

        user = None
        # check if user already exist
        try:
            user = Account.objects.get(email=email)
        except:
            pass
        if user:
            messages.error(request, 'This email is already registered.')

        if user is None and form.is_valid():
            # holding a instance before saving to protect from case sensitive username
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User account was created!')
            # sets session for user
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Error has occurred during registration')

    return render(request, 'accounts/register-login.html', context)

 
def loginAccount(request):
    # check for session in cookie to check if already logged in
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        # request.method is a dictionary of all the data in POST
        email = request.POST['email']
        password = request.POST['password']

        # to check if user exist in database
        try:
            user = Account.objects.get(email=email)
        except:
            # for flashing messages
            messages.error(request, 'Email doesnt exist')

        # this check password against username in database
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # sets session for user
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email or Password is incorrect')

    return render(request, 'accounts/register-login.html')


def logoutAccount(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')

@login_required(login_url='login')
def dashAccount(request):
    return render(request, 'accounts/dashboard.html')
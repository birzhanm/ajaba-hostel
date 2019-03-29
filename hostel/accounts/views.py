from .forms import SignUpForm, SignInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.id_number = form.cleaned_data.get('id_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('rooms:block_list')
        else:
            messages.error(request, 'Please correct the following errors')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

def signin(request):
    if request.method == "POST":
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('rooms:block_list')
        else:
            messages.error(request, 'Please correct the following errors')
    else:
        form = SignInForm()
    context = {'form': form}
    return render(request, 'accounts/signin.html', context)

def signout(request):
    logout(request)
    return redirect('rooms:block_list')

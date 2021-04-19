from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, UserprofileForm

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        userprofileform = UserprofileForm(request.POST)

        if form.is_valid() and userprofileform.is_valid():
            user = form.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            userprofile.save()

            login(request, user)

            return redirect('core:frontpage')
    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()

    return render(request, 'signup.html', {'form': form, 'userprofileform': userprofileform })

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')
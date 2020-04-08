from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login



def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    context = {}
    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = get_user_model().objects.create_user(
                username=username, password=password
            )
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            context['form'] = form
    else:
        context['form'] = SignUpForm()

    return render(
        request,
        'signup.html',
        context
    )

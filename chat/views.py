from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect


User = get_user_model()


def user_list(request):
    """
    NOTE: This is fine for demonstration purposes, but this should be
    refactored before we deploy this app to production.
    Imagine how 100,000 users logging in and out of our app would affect
    the performance of this code!
    """
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'user_list.html', {'users': users})


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('chat:user_list'))
        else:
            print(form.errors)
    return render(request, 'log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('chat:log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('chat:log_in'))
        else:
            print(form.errors)
    return render(request, 'sign_up.html', {'form': form})

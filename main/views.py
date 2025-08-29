from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, AvatarForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html', {'title': 'Main page'})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} ({email}): {message}") 
    return render(request, 'main/contact.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar updated successfully!')
            return redirect('profile')
    else:
        form = AvatarForm(instance=request.user.profile)

    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'main/profile.html', context)

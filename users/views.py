from django.shortcuts import render, redirect
from django.contrib import messages #for flash message, one time alert to templates, disapper on next request
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #instantiate the form with post data
        if form.is_valid():
            form.save() #hash the password, and do the backend stuff
            username = form.cleaned_data.get('username') #validated form data will be in form.cleaned_data dictionary
            messages.success(request, f'Your account is created! Please Login!')
            return redirect('blog-home') #url patter for bloghomepage
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #file data coming in with POST data

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your accound has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

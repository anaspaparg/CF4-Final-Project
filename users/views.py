from django.shortcuts import render, redirect
from . forms import RegistrationUserForm


def register(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        RegistrationUserForm()

    form = RegistrationUserForm()
    return render(request, 'users/register.html', {'form': form})

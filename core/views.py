from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm

# Create your views here.
def frontPage(request):
    return render(request, 'core/frontPage.html')

def signUp(request):
    # Check if the form has been submitted or not
    if request.method == 'POST':
        # Form has been clicked
        form = SignUpForm(request.POST)

        # Check if form is valid -> username is there & passwords are matching
        if form.is_valid():
            user = form.save() # Create user

            login(request, user) # Authenticate the user

            return redirect('frontPage')
    else:
        # Create a empty instance of signup form
        form = SignUpForm()

    return render(request, 'core/signUp.html', {'form': form})
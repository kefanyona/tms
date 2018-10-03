from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

# Notification after speedometer counters 5000km

from .forms import AssignmentForm


def assignment_details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #  create a form instance and populate it with data
        form = AssignmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form._cleaned data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks')
    else:
        form = AssignmentForm()

    return render(request, 'home.html', {'form' : form})

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def evalindex(request):
    '''Currently returns underconstruction page'''

    return render(
        request,
        'evalindex.html'
    )

def thanks(request):
    return render(
        request, 
        'thanks.html'
    )

from .forms import EvaluationForm

def evaluate_workshop(request):
    """
    View function for evaluating a workshop
    """

    if request.method == 'POST':
        # if this is a POST request we need to process the form data
        #form = EvaluateWorkshopForm(request.POST)
        form = EvaluationForm(request.POST)
        # check weather it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        form = EvaluationForm()

    return render(request, 'evaluate.html', {'form': form})
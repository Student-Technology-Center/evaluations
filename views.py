from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *
import datetime

# Create your views here.

def index(request):
    '''
    Currently returns underconstruction page
    '''

    return render(request, 'eval_index.html')

def evaluate_workshop(request, workshop_name, instructor_name):
    '''
    View function for evaluating a workshop
    '''

    # Default form values
    defaults = {
        'instructor_name': instructor_name.replace("_", " "),
        'workshop_name': workshop_name.replace("_", " "),
        'workshop_date': datetime.datetime.now(),
    }

    if request.method == 'POST':

        # if this is a POST request we need to process the form data
        form = EvaluationForm(request.POST, initial=defaults)

        # check weather it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request, 'eval_thanks.html')

    else:
        form = EvaluationForm(initial=defaults)

    return render(request, 'eval_evaluate.html', {'form': form})

def evaluate_workshop_blank(request):
    '''
    Overload for the evaluate_workshop function when no arguments are provided
    '''
    return evaluate_workshop(request, "", "")

def view(request):
    '''
    View function for viewing workshop evaluations
    '''

    query_results = Evaluation.objects.all().order_by('-workshop_date')

    return render(request, 'eval_view.html', {'query_results': query_results})

class EvalDeleteView(DeleteView):
    model = Evaluation 
    success_url = reverse_lazy('evaluate-view')
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *

# Create your views here.

def index(request):
    '''
    Currently returns underconstruction page
    '''

    return render(request, 'eval_index.html')

def evaluate_workshop(request):
    '''
    View function for evaluating a workshop
    '''

    if request.method == 'POST':
        # if this is a POST request we need to process the form data
        #form = EvaluateWorkshopForm(request.POST)
        form = EvaluationForm(request.POST)

        # check weather it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request, 'eval_thanks.html')

    else:
        form = EvaluationForm()

    return render(request, 'eval_evaluate.html', {'form': form})

def view(request):
    '''
    View function for viewing workshop evaluations
    '''

    query_results = Evaluation.objects.all().order_by('-workshop_date')

    return render(request, 'eval_view.html', {'query_results': query_results})

class EvalDeleteView(DeleteView):
    model = Evaluation 
    success_url = reverse_lazy('evaluate-view')
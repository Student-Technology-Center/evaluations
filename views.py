from django.shortcuts import render

# Create your views here.

def evalindex(request):
    '''Currently returns underconstruction page'''

    return render(
        request,
        'evalindex.html'
    )
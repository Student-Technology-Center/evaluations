from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 


from evaluations.models import Evaluation

class DateInput(forms.DateInput):
    input_type = 'date'

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = '__all__'
        widgets = {
            'workshop_date': DateInput(),
        }

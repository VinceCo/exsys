from django import forms
from django.forms import ModelForm
from django.forms import RadioSelect
from django.forms import Textarea
from . import models


#class EnergyForm(forms.Form):
#    energy_value = forms.DecimalField(min_value=None,
#                               max_digits=19,
#                               decimal_places=10)
#
"""
Apparemment il faut utiliser
le widget attribut pour changer
le widget original.
"""
class EnergyForm(ModelForm):
    class Meta:
        model = models.Energy
        fields = ['resource', 'unit', 'value']
        widgets = {'resource': forms.RadioSelect}
#        fields = '__all__'

#class MachineForm(ModelForm):
#    class Meta:
#        model = models.Machine
#        fields = ['name', 'efficiency',]
##        widgets = {'name': forms.RadioSelect}

class MachineForm(forms.Form):
#    name = forms.ChoiceField(widget=forms.RadioSelect)
    name = forms.ChoiceField(widget=forms.RadioSelect)

#CHOICES = [('1', 'First'),('2', 'Second')]
class TestForm(forms.Form):
    energy = forms.ChoiceField(widget=forms.RadioSelect)
    unit = forms.ChoiceField(widget=forms.RadioSelect)
    value = forms.FloatField()
    name = forms.ChoiceField(widget=forms.RadioSelect)

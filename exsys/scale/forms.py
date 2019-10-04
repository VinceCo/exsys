from django import forms
from django.forms import ModelForm
from django.forms import RadioSelect
from django.forms import Textarea
from . import models


class ScaleForm(forms.Form):
    energy = forms.ModelChoiceField(queryset=
                                        models.Energy.resource.get_queryset(),
                                        empty_label=None,
                                        widget=forms.RadioSelect
                                       )
    unit = forms.ModelChoiceField(
        queryset=models.Unit.objects.filter(
            physical_quantity__physical_quantity="energy"),
        empty_label=None,
        widget=forms.RadioSelect)
    value = forms.FloatField()
    machine = forms.ModelChoiceField(
        queryset=models.Machine.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect)
    efficiency = forms.FloatField()
    height_scale = forms.ModelChoiceField(
        queryset=models.HeightScale.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect)

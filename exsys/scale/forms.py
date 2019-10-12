from django import forms
from django.forms import ModelForm
from django.forms import RadioSelect
from django.forms import Textarea
from django.db.models import Q
from . import models


class EnergyForm(forms.Form):
    energy = forms.ModelChoiceField(queryset=
                                        models.Energy.resource.get_queryset(),
                                        empty_label=None,
                                        widget=forms.RadioSelect
                                       )
    unit = forms.ModelChoiceField(
        queryset=models.Unit.objects.filter(
            Q(physical_quantity__physical_quantity="energy")
            | Q(physical_quantity__physical_quantity="volume")),
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

class MachinePowerForm(forms.Form):
    machine = forms.ModelChoiceField(
        queryset=models.Machine.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect)
    power = forms.DecimalField()
    power_unit = forms.ModelChoiceField(
        queryset=models.Unit.objects.filter(
            physical_quantity__physical_quantity="power"),
        empty_label=None,
        widget=forms.RadioSelect)
    efficiency = forms.FloatField(min_value=0, max_value=1)
    time = forms.DecimalField()
    time_unit = forms.ModelChoiceField(
        queryset=models.Unit.objects.filter(
            physical_quantity__physical_quantity="time"),
        empty_label=None,
        widget=forms.RadioSelect)
    height_scale = forms.ModelChoiceField(
        queryset=models.HeightScale.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect)

class MachineConsumptionForm(forms.Form):
    machine = forms.ModelChoiceField(
        queryset=models.Machine.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect)
    # Be careful, I should try to find a way to
    # filter the rights fuel, not the energy because
    # maybe I would endup with uranium in the list...
    fuel = forms.ModelChoiceField(queryset=models.Energy.resource.get_queryset(),
                                  empty_label=None,
                                  widget=forms.RadioSelect)
    consumption = forms.DecimalField()
    consumption_unit = forms.ModelChoiceField(
        queryset=models.Unit.objects.filter(
            physical_quantity__physical_quantity="energy consumption per distance"),
        empty_label=None,
        widget=forms.RadioSelect)
    distance = forms.DecimalField()
    distance_unit = forms.ModelChoiceField(
        queryset=models.Unit.objects.filter(
            physical_quantity__physical_quantity="distance"),
        empty_label=None,
        widget=forms.RadioSelect)
    height_scale = forms.ModelChoiceField(
        queryset=models.HeightScale.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect)

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.forms import formset_factory
from django.forms import ChoiceField
from django.forms import RadioSelect
from . import models
from . import forms
from . import methods


def home(request):
    if (request.method == 'POST'):
        scale_form = forms.ScaleForm(request.POST)
        if scale_form.is_valid():
            machine_output_energy = methods.machine_output_energy(
                scale_form.cleaned_data['value'],
                scale_form.cleaned_data['efficiency'])
            height_potential = methods.energy_into_height_potential(
                machine_output_energy)
            height_equivalent = methods.height_into_height_scale(
                height_potential,
                models.HeightScale.objects.get(
                    id=request.POST["height_scale"]))
            output = height_equivalent
    else:
        scale_form = forms.ScaleForm()
        output_energy = 0
    return render(request, 'scale/scale.html', locals())

def redirect_home(request):
    return redirect('home')

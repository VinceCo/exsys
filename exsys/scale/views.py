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
    return render(request, 'scale/home.html', locals())

def energy(request):
    url = "energy"
    if (request.method == 'POST'):
        form = forms.EnergyForm(request.POST)
        if form.is_valid():
            machine_output_energy = methods.machine_output_energy(
                models.Energy.objects.get(
                    resource=form.cleaned_data['energy']),
                form.cleaned_data['value'],
                models.Unit.objects.get(symbol=form.cleaned_data['unit']),
                form.cleaned_data['efficiency'])

            height_potential = methods.energy_into_height_potential(
                machine_output_energy)

            height_equivalent = methods.height_into_height_scale(
                height_potential,
                models.HeightScale.objects.get(
                    id=request.POST["height_scale"]))

            output = height_equivalent
    else:
        form = forms.EnergyForm()
        output_energy = 0
    return render(request, 'scale/form.html', locals())

def machine(request):
    return render(request, 'scale/machine.html', locals())

def machine_consumption(request):
    url = "machine_consumption"
    if (request.method == 'POST'):
        form = forms.MachineConsumptionForm(request.POST)
        if form.is_valid():

            energy = methods.consumption_into_energy(
                models.Energy.objects.get(resource__name=
                                          form.cleaned_data["fuel"]),
                form.cleaned_data["consumption"],
                form.cleaned_data["consumption_unit"],
                form.cleaned_data["distance"],
                form.cleaned_data["distance_unit"],
                models.ConversionCoefficient,
            )
#            print('form.cleaned_data["power"] : ', form.cleaned_data["power"])
#            print('form.cleaned_data["power_unit"] : ',
#                  form.cleaned_data["power_unit"])
#            energy = methods.power_into_energy(
#                form.cleaned_data["power"],
#                form.cleaned_data["power_unit"],
#                form.cleaned_data["time"],
#                form.cleaned_data["time_unit"],
#                models.ConversionCoefficient.objects.filter(
#                    unit_from__symbol="ch").filter(
#                        unit_to__symbol="W"))
#                models.ConversionCoefficient.objects.filter(
#                    unit_from__symbol=form.cleaned_data["power_unit"]).filter(
#                        unit_to__symbol="W"))
#                models.ConversionCoefficient,
#                form.cleaned_data["efficiency"],)

            height_potential = methods.energy_into_height_potential(
                energy)

            height_equivalent = methods.height_into_height_scale(
                height_potential,
                models.HeightScale.objects.get(
                    id=request.POST["height_scale"]))
            output = height_equivalent
    else:
        form = forms.MachineConsumptionForm()
    return render(request, 'scale/form.html', locals())

def machine_power(request):
    url = "machine_power"
    if (request.method == 'POST'):
        form = forms.MachinePowerForm(request.POST)
        if form.is_valid():
            print('form.cleaned_data["power"] : ', form.cleaned_data["power"])
            print('form.cleaned_data["power_unit"] : ',
                  form.cleaned_data["power_unit"])
            energy = methods.power_into_energy(
                form.cleaned_data["power"],
                form.cleaned_data["power_unit"],
                form.cleaned_data["time"],
                form.cleaned_data["time_unit"],
                models.ConversionCoefficient,
                form.cleaned_data["efficiency"],)
            height_potential = methods.energy_into_height_potential(
                energy)
            height_equivalent = methods.height_into_height_scale(
                height_potential,
                models.HeightScale.objects.get(
                    id=request.POST["height_scale"]))
            output = height_equivalent
    else:
        form = forms.MachinePowerForm()
    return render(request, 'scale/form.html', locals())

def redirect_home(request):
    return redirect('home')

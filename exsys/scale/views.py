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

#        # Voir comment avoir accès au formulaire via le post.
#        # Est ce que c'est via un dictionnaire ou non ?
##        test_form = prerare_form_test()
        test_form = forms.TestForm(request.POST)
        print('request.POST', request.POST)
        print('request.content_type', request.content_type)
        print('request.path', request.path)
        print('request.path_info', request.path_info)
        print('request.content_type', request.content_type)
        print('request.scheme', request.scheme)
        print('request.get_full_path_info()', request.get_full_path_info())
        print('test_form', test_form)
        if test_form.is_valid():
            print("yoooooolooooo")
            """
            Il faut ici que je récupère les données pour les envoyer
            à la bonne méthode.
            Je dois avoir la quantité d'énergie final après quelle soit dissipé
            par la machine ET son équivalent en energie musculaire humaine.
            """
            machine_output_energy = methods.machine_output_energy(
                test_form.cleaned_data['value'],
                test_form.cleaned_data['efficiency'])

            height_potential = methods.energy_into_height_potential(
                machine_output_energy)

            # Il faudra choisir les équivalances.
            height_equivalent = methods.height_into_height_scale(
                height_potential, 'Tour Eiffel')

            output = height_equivalent


#        machine_form = forms.EnergyForm(request.POST)
#        if energy_form.is_valid():
            # Il faut ici que je récupère les données pour les envoyer 
            # à la bonne méthode.
            # Je dois avoir la quantité d'énergie final après quelle soit dissipé
            # par la machine ET son équivalent en energie musculaire humaine.
#            machine_output_energy = machine_output_energy(
#                energy_form.cleaned_data['value']
#                * machine_form.cleaned_data['efficiency'])
#            height_potential = energy_into_height_potential(
#                machine_output_energy)
#            height_equivalent = height_into_height_scale(
#                height_potential, 'tour eiffel')
            #Remarque : il faudrait proposer des échelles à l'utilisateur.
            #energy_value = form.cleaned_data['energy_value']
            # else:
                # energy_form.fields['resource'] = ChoiceField(widget=RadioSelect,
                                                             # choices=resource_list)
                # energy_form.fields['unit'] = ChoiceField(widget=RadioSelect,
                                                         # choices=unit_list)
        # #        energy_form = EnergyFormSet()
        # #        energy_form = EnergyFormSet(initial=initial_energy)
    else:
        test_form = forms.TestForm()
#        test_form = prerare_test_form()

#        unit_set =  models.Unit.objects.filter(
#            physical_quantity__physical_quantity="energy")
#        unit_list = []
#        for unit in unit_set:
#            tuple_unit = unit.id, unit.unit
#            unit_list.append(tuple_unit)
#
#        print('unit_list', unit_list)
#        energy_set = models.Energy.objects.all()
#        resource_list = []
#        for energy in energy_set:
#            resource_list.append((energy.id, energy.resource.name))
#        print('resource_list', resource_list)
#
##        energy_form = forms.EnergyForm()
##        energy_form.fields['resource'] = ChoiceField(widget=RadioSelect,
##                                                     choices=resource_list)
##        energy_form.fields['unit'] = ChoiceField(widget=RadioSelect,
##                                                 choices=unit_list)
#
#        machine_set = models.Machine.objects.all()
#        machine_list = []
#        for machine in machine_set:
#            machine_list.append((machine.id, machine.name))
#        machine_form = forms.MachineForm()
##        machine_form.fields['name'] = ChoiceField(widget=RadioSelect,
##                                                  choices=machine_list)
#
#        test_form = forms.TestForm()
#        test_form.fields['energy'] = ChoiceField(widget=RadioSelect,
#                                                 choices=resource_list)
#        test_form.fields['unit'] = ChoiceField(widget=RadioSelect,
#                                               choices=unit_list)
#
#        test_form.fields['name'] = ChoiceField(widget=RadioSelect,
#                                               choices=machine_list)
        output_energy = 0

    return render(request, 'scale/scale.html', locals())

def prerare_test_form():
    """
    Prepare the test form.
    """
    print("Je suis dans prepare_test_form")

    unit_set =  models.Unit.objects.filter(
        physical_quantity__physical_quantity="energy")
    unit_list = []
    for unit in unit_set:
        tuple_unit = unit.id, unit.unit
        unit_list.append(tuple_unit)
    print('unit_list', unit_list)

    energy_set = models.Energy.objects.all()
    resource_list = []
    for energy in energy_set:
        resource_list.append((energy.id, energy.resource.name))
    print('resource_list', resource_list)

    machine_set = models.Machine.objects.all()
    machine_list = []
    for machine in machine_set:
        machine_list.append((machine.id, machine.name))
    print('machine', machine_list)

    test_form = forms.TestForm()
    test_form.fields['energy'] = ChoiceField(widget=RadioSelect,
                                             choices=resource_list)
    test_form.fields['unit'] = ChoiceField(widget=RadioSelect,
                                           choices=unit_list)

    test_form.fields['name'] = ChoiceField(widget=RadioSelect,
                                           choices=machine_list)
    print("test_from : ", test_form)
    return test_form

def home_energy(request):
    # On gere le formulaire energy
    pass

def home_machine(request):
    # On gere le formulaire machine
    pass


# Ou alors je fais un méga formulaire.
# C'est peut être plus simple.



#def home(request):
#    unit_set =  models.Unit.objects.filter(
#        physical_quantity__physical_quantity="energy")
#    unit_list = []
#    for unit in unit_set:
#        tuple_unit = unit.id, unit.unit
#        unit_list.append(tuple_unit)
##    unit_list = models.Unit.objects.filter(
##        physical_quantity__physical_quantity="energy")
#
#    print('unit_list', unit_list)
#    energy_set = models.Energy.objects.all()
#    resource_list = []
#    for energy in energy_set:
#        resource_list.append((energy.id, energy.resource.name))
#    print('resource_list', resource_list)
#
#    energy_form = forms.EnergyForm()
#    energy_form.fields['resource'] = ChoiceField(widget=RadioSelect,
#                                                 choices=resource_list)
#    energy_form.fields['unit'] = ChoiceField(widget=RadioSelect,
#                                             choices=unit_list)
#
##    initial = {'resource': resource_list,
##               'unit': unit_list,
##               'value': 0}
#
#    machine_set = models.Machine.objects.all()
#    machine_list = []
#    for machine in machine_set:
#        machine_list.append((machine.id, machine.name))
##    car_list = [(1, "Car")]
##    machine_form = forms.MachineForm(initial={'name': car_list})
#    machine_form = forms.MachineForm()
#    machine_form.fields['name'] = ChoiceField(widget=RadioSelect,
#                                              choices=machine_list)
#
#    if energy_form.is_valid():
##        energy_value = form.cleaned_data['energy_value']
#        pass
#    else:
#        energy_form.fields['resource'] = ChoiceField(widget=RadioSelect,
#                                                     choices=resource_list)
#        energy_form.fields['unit'] = ChoiceField(widget=RadioSelect,
#                                                 choices=unit_list)
##        energy_form = EnergyFormSet()
##        energy_form = EnergyFormSet(initial=initial_energy)
#
#    value = 42
#    input_energy = models.Energy.objects.order_by('resource__name')
#    machine = models.Machine.objects.all()
#    output_energy = 42
#    return render(request, 'scale/scale.html', locals())


def redirect_home(request):
    return redirect('home')

# Comment calcule l'énergie ?
def energy_into_height_potential(energy, height_scale):
    """
    Using equation : m*g*h
    mass times gravity acceleration times height.
    """
    #gravity in m.s^-2
    g = models.PhysicalConstant.object.get(name="Earth's gravity")
    human = models.Human.object.all()[0]
    height_equivalent = energy / (g * human.weight)

def height_into_height_scale(height, scale_name):
    height_scale = models.HeightScale.objects.get(name=scale_name)
    # Faire le round ?
    return height / height_scale

def energy_into_volume_soil_digged(energy, human_power):
    """
    For a energy given, give the equivalent volume of soil digged
    if this energy is used for digging soil over 1m height profond.
    """
    # connais pas la masse volumique du sol, on va dire 1.8 tonne/m^3
    # Dig over 1 metre height
    height = 1
    # bulk_density_soil * soil_volume_digged * g * height = energy
    soil_volume_digged = energy / (bulk_density_soil * g * height)
    return soil_volume_digged

def climbing_into_energy(height):
    """
    Return in Joule the energy consumme
    by a human when climbing over height meters
    height must be in metres.
    """
    human = models.Human.object.all()[0]
    g = models.PhysicalConstant.objects.get(name="Earth's gravity")
    result = height * human.weight * g
    return result
 #Il faudrait proposer à la page scale.html les différentes echelle


"""
1 litre d'essence ==> X kWh ==> X pairs de bras faisant Y activité
1 voiture de Xkg, roulant à Y km/h ==> A kWh ==> Z pairs de bras faisant P activité.
"""

def test(request):
    CHOICES = [('1', 'First'),('2', 'Second')]

#    TestFormSet = formset_factory(forms.TestForm)
#    formset = forms.TestForm(initial= [{'radio': CHOICES}])

#    data = {'radio': CHOICES}
#    formset = forms.TestForm(data)

#    data = {'mot': "yolo"}
#    formset = forms.TestForm(data)


#    return render(request, 'scale/test.html', locals())
#    formset = forms.TestForm(initial={'radio': [('1', 'First'),
#                                             ('2', 'Second')]})

#    choices = [('1', 'First'),('2', 'Second')]
#    formset = forms.TestForm(choices)

#    CHOICES = [('1', 'First'),('2', 'Second')]
#    formset = forms.TestForm()
#    formset.radio = CHOICES
#    print(formset)
#    formset = forms.TestForm()

#    formset = forms.TestForm(models.Unit.objects.all())
    # https://docs.djangoproject.com/en/2.2/ref/forms/fields/#fields-which-handle-relationships
    formset = forms.TestForm()
    formset.fields['radio'] = ChoiceField(widget=RadioSelect, choices=CHOICES)
    return render(request, 'scale/test.html', locals())

#def machine_output_energy(input_energy, efficiency):
#    return input_energy * efficiency

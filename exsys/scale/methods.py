from . import models

def machine_output_energy(input_energy, efficiency):
    return input_energy * efficiency

#def energy_into_height_potential(energy, height_scale):
def energy_into_height_potential(energy):
    """
    I delete the height_scale
    """
    """
    Using equation : m*g*h
    mass times gravity acceleration times height.
    """
    #gravity in m.s^-2
    g = float(models.PhysicalConstant.objects.get(name="Earth's gravity").value)
    human = float(models.Human.objects.all()[0].weight)
    height_equivalent = energy / (g * human)
    return height_equivalent

def height_into_height_scale(height, scale_name):
    height_scale = float(models.HeightScale.objects.get(name=scale_name).height)
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

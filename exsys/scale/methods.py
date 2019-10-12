from . import models

#def machine_output_energy(energy, value, unit, efficiency):
#    if unit.physical_quantity.physical_quantity == "volume":
#        if unit.symbol == "m^3":
#            energy_input = float(energy.energy_density) * value
#        if unit.symbol == "l":
#            energy_input = float(energy.energy_density) * value * 1E-3
#    elif unit.physical_quantity.physical_quantity == "energy":
#        if unit.symbol == "J":
#           energy_input = value
#
#    return energy_input * efficiency

def get_coef_conversion(unit_from, unit_to):
    unit_convertor = models.ConversionCoefficient
    return float(unit_convertor.objects.filter(
            unit_from__symbol=unit_from).filter(
                unit_to__symbol=unit_to)[0].value)

def machine_output_energy(energy, value, unit, efficiency):
#    if unit.physical_quantity.physical_quantity == "volume":
#        if unit.symbol == "m^3":
#            energy_input = float(energy.energy_density) * value
#        if unit.symbol == "l":
#            energy_input = float(energy.energy_density) * value * 1E-3
#    elif unit.physical_quantity.physical_quantity == "energy":
#        if unit.symbol == "J":
#           energy_input = value

#   coef_conversion = float(unit_convertor.objects.filter(
#        unit_from__symbol=unit).filter(
#            unit_to__symbol="m^3")[0].value)

    if unit.physical_quantity.physical_quantity == "volume":
        coef_conversion = get_coef_conversion(unit, "m^3")
        value_m3 = value * coef_conversion
        energy_in_J = float(energy.energy_density) * value_m3 * efficiency
    elif unit.physical_quantity.physical_quantity == "energy":
        coef_conversion = get_coef_conversion(unit, "J")
        energy_in_J = value * coef_conversion * efficiency

    return energy_in_J


def energy_into_height_potential(energy):
    """
    Convert an energy into height using
    the equation of height energy potential.
    Using equation : m*g*h
    mass times gravity acceleration times height.
    """
    #gravity in m.s^-2
    g = float(models.PhysicalConstant.objects.get(name="Earth's gravity").value)
    human = float(models.Human.objects.all()[0].weight)
    height_equivalent = energy / (g * human)
    return height_equivalent

def height_into_height_scale(height, height_scale):
    """
    Convert the height into a height scale.
    """
    height_scale = float(height_scale.height)
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

def power_into_energy(power, power_unit, time, time_unit,
                      unit_convertor, efficiency):
    """
    Convert the power of a machine working over a time
    into energy.
    """
    # It is durtier BUT
    # at least the will be no conflict
    # betweens to different coefficient
#    coef_conversion = float(unit_convertor.objects.filter(
#        unit_from__symbol=power_unit).filter(
#            unit_to__symbol="W")[0].value)
    coef_conversion = get_coef_conversion(power_unit, "W")
    power_in_W = float(power) * coef_conversion

#    coef_conversion = float(unit_convertor.objects.filter(
#        unit_from__symbol=time_unit).filter(
#            unit_to__symbol="s")[0].value)
    coef_conversion = get_coef_conversion(time_unit, "s")
    time_in_s = float(time) * coef_conversion

    energy_in_J = power_in_W * time_in_s
    # Taking into account the efficiency of
    # the machine.
    energy_in_J = energy_in_J * efficiency
    unit = "J"
    return energy_in_J


def consumption_into_energy(fuel, consumption, consumption_unit, distance,
                            distance_unit, unit_convertor):
    """
    Convert a consumption (in litre of a fuel) into energy
    """
#    coef_conv_l_per_100_km = float(unit_convertor.objects.filter(
#        unit_from__symbol=consumption_unit).filter(
#            unit_to__symbol="l/100km")[0].value)
    coef_conv_l_per_100_km = get_coef_conversion(consumption_unit, "l/100km")
    consumption_l_per_100_km = float(consumption) * coef_conv_l_per_100_km
    print("consumption_l_per_100_km : ", consumption_l_per_100_km)

#    coef_conv_into_km = float(unit_convertor.objects.filter(
#        unit_from__symbol=distance_unit).filter(
#            unit_to__symbol="km")[0].value)
    coef_conv_into_km = get_coef_conversion(distance_unit, "km")
    distance_in_km = float(distance) * coef_conv_into_km
    print("distance_in_km : ",  distance_in_km)

    consumption_l = consumption_l_per_100_km * distance_in_km/100
    print("consumption_l : ",  consumption_l)

#    coef_conv_l_into_m3 = 1/float(unit_convertor.objects.filter(
#        unit_from__symbol="m^3").filter(
#            unit_to__symbol="l")[0].value)
    coef_conv_l_into_m3 = get_coef_conversion("l", "m^3")
    consumption_m3 = consumption_l * coef_conv_l_into_m3
    print("consumption_m3 : ",  consumption_m3)

    energy = float(fuel.energy_density) * consumption_m3
    print("energy : ",  energy)

    return energy

def energy_into_height_equivalent(energy, height_scale):
    """
    Gives the equivalent of energy into
    height of the height scale chosen.
    """
    height_potential = energy_into_height_potential(
        energy)
    height_equivalent = height_into_height_scale(
        height_potential,
        models.HeightScale.objects.get(
                    id=height_scale))
    output = height_equivalent
    return output

from . import models

def machine_output_energy(energy, value, unit, efficiency):
    if unit.physical_quantity.physical_quantity == "volume":
        if unit.symbol == "m^3":
            energy_input = float(energy.energy_density) * value
        if unit.symbol == "l":
            energy_input = float(energy.energy_density) * value * 1E-3
    elif unit.physical_quantity.physical_quantity == "energy":
        if unit.symbol == "J":
           energy_input = value

    return energy_input * efficiency

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

def height_into_height_scale(height, height_scale):
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
    print("time_unit : ", time_unit)
#    print('models.ConversionCoefficient.objects.filter( \
#        unit_from=time_unit).filter(unit_to="s")', models.ConversionCoefficient.objects.filter(
#            unit_from=time_unit).filter(unit_to="s"))
#
#    conv_temps = float(models.ConversionCoefficient.objects.filter(
#        unit_from__symbol=time_unit).filter(unit_to__symbol="s").value)
#
#    conv_power = float(unit_convertor.objects.filter(
#        unit_from=power_unit,
#        unit_to="W").value)
#    print("conv_temps : ",conv_temps)
#    print("conv_power : ",conv_power)

#    conv_power = float(unit_convertor.objects.filter(
#        unit_from=power_unit,
#        unit_to="W",).value)
#    conv_temps = float(unit_convertor.objects.filter(
#        unit_from=time_unit,
#        unit_to="s",).value)

#    # Remarque : the folowing block works BUT
#    # be carreful with the get, because if there is 
#    # a conversion coefficient from ch to kW, it will
#    # raise an error
#    power_in_W = float(power) * float(unit_convertor.objects.get(
#        unit_from=power_unit).value)
#    time_in_s = float(time) * float(unit_convertor.objects.get(
#        unit_from=time_unit).value)

    # It is more durty BUT
    # at least the will be no conflict
    # betweens to different coefficient
    coef_conversion = float(unit_convertor.objects.filter(
        unit_from__symbol=power_unit).filter(
            unit_to__symbol="W")[0].value)
    power_in_W = float(power) * coef_conversion

    coef_conversion = float(unit_convertor.objects.filter(
        unit_from__symbol=time_unit).filter(
            unit_to__symbol="s")[0].value)
    time_in_s = float(time) * coef_conversion

#    power_in_W = (float(power)
#                  * float(unit_convertor.objects.filter(
#                      unit_from__symbol=power_unit).filter(
#                          unit_to__symbol="W")[0].value))
#    time_in_s = float(time) * float(unit_convertor.objects.filter(
#        unit_from__symbol=time_unit).filter(unit_to__symbol="s")[0].value)

#    time_in_s = float(time) * float(unit_convertor.objects.filter(
#        unit_from=time_unit).filter(unit_to="s",)[0].value)
#    print("power_in_W : ", power_in_W)
#    print("time_in_s : ", time_in_s)

    energy_in_J = power_in_W * time_in_s
    # Taking into account the efficiency of
    # the machine.
    energy_in_J = energy_in_J * efficiency
    unit = "J"
#    print("energy_in_J : ", energy_in_J)
#    return (energy, unit)
    return energy_in_J


def consumption_into_energy(fuel, consumption, consumption_unit, distance,
                            distance_unit, unit_convertor):
#    fuel = models.Energy.objects.get(name=fuel)
#    fuel_energy_density = fuel.energy_density
#    fuel_energy_density_unit = fuel.energy_density_unit

    coef_conv_l_per_100_km = float(unit_convertor.objects.filter(
        unit_from__symbol=consumption_unit).filter(
            unit_to__symbol="l/100km")[0].value)
    consumption_l_per_100_km = float(consumption) * coef_conv_l_per_100_km
    print("consumption_l_per_100_km : ", consumption_l_per_100_km)

    coef_conv_into_km = float(unit_convertor.objects.filter(
        unit_from__symbol=distance_unit).filter(
            unit_to__symbol="km")[0].value)
    distance_in_km = float(distance) * coef_conv_into_km
    print("distance_in_km : ",  distance_in_km)

    consumption_l = consumption_l_per_100_km * distance_in_km/100
    print("consumption_l : ",  consumption_l)

    coef_conv_l_into_m3 = 1/float(unit_convertor.objects.filter(
        unit_from__symbol="m^3").filter(
            unit_to__symbol="l")[0].value)
    consumption_m3 = consumption_l * coef_conv_l_into_m3
    print("consumption_m3 : ",  consumption_m3)

    energy = float(fuel.energy_density) * consumption_m3
    print("energy : ",  energy)

    return energy

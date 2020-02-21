from tools import models

"""
Use this script like this
python manage.py shell < script.py
"""

def delete_object(object_list):
    for item in object_list:
        item.delete()


# Reference
Reference = models.Reference
delete_object(Reference.objects.all())
url_list = ["https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php",
            "",
            "https://en.wikipedia.org/wiki/Energy_density",
            "https://neutrium.net/properties/specific-energy-and-energy-density-of-fuels/",
           ]
book_list =["",
            "BP Statistical review of world energy",
            "",
            "",
           ]
for k in range(0, len(url_list)):
    item = Reference(url=url_list[k], book=book_list[k])
    item.save()
print("\n", Reference.objects.all())


# Physical state
PhysicalState = models.PhysicalState
delete_object(PhysicalState.objects.all())
state_list = ["solid", "liquid", "gas"]
for state in state_list:
    item = PhysicalState(state=state)
    item.save()
print("\n", PhysicalState.objects.all())


# Physical quantity
PhysicalQuantity = models.PhysicalQuantity
delete_object(PhysicalQuantity.objects.all())
quantitys = ["energy",
             "mass",
             "volume",
             "density",
             "specific volume",
             "power",
             "energy density",
             "specific energy",
             "speed",
             "acceleration",
             "distance",
             "energy consumption per distance",
             "time",
            ]
for quantity in quantitys:
    item = PhysicalQuantity(physical_quantity=quantity)
    item.save()
print("\n", PhysicalQuantity.objects.all())


# Unit
Unit = models.Unit
delete_object(Unit.objects.all())
unit_list = ["joule",
             "kilogram",
             "cubic metre",
             "litre",
             "kilogram per cubic metre",
             "cubic metre per kilogram",
             "watt",
             "kilo-watt",
             "cheval-vapeur",
             "joule per cubic metre",
             "joule per kilogram",
             "metre per second",
             "metre per second squared",
             "metre",
             "kilometre",
             "litre per 100km",
             "seconde",
             "hour",
            ]
symbol_list = ["J",
               "kg",
               "m^3",
               "l",
               "kg/m^3",
               "m^3/kg",
               "W",
               "kW",
               "ch",
               "J/m^3",
               "J/kg",
               "m/s",
               "m/s^(-2)",
               "m",
               "km",
               "l/100km",
               "s",
               "h",
              ]
physical_quantity_list = [
    PhysicalQuantity.objects.get(physical_quantity="energy"),
    PhysicalQuantity.objects.get(physical_quantity="mass"),
    PhysicalQuantity.objects.get(physical_quantity="volume"),
    PhysicalQuantity.objects.get(physical_quantity="volume"),
    PhysicalQuantity.objects.get(physical_quantity="density"),
    PhysicalQuantity.objects.get(physical_quantity="specific volume"),
    PhysicalQuantity.objects.get(physical_quantity="power"),
    PhysicalQuantity.objects.get(physical_quantity="power"),
    PhysicalQuantity.objects.get(physical_quantity="power"),
    PhysicalQuantity.objects.get(physical_quantity="energy density"),
    PhysicalQuantity.objects.get(physical_quantity="specific energy"),
    PhysicalQuantity.objects.get(physical_quantity="speed"),
    PhysicalQuantity.objects.get(physical_quantity="acceleration"),
    PhysicalQuantity.objects.get(physical_quantity="distance"),
    PhysicalQuantity.objects.get(physical_quantity="distance"),
    PhysicalQuantity.objects.get(physical_quantity="energy consumption per distance"),
    PhysicalQuantity.objects.get(physical_quantity="time"),
    PhysicalQuantity.objects.get(physical_quantity="time"),
]
for k in range(0, len(unit_list)):
    item = Unit(unit=unit_list[k],
                symbol=symbol_list[k],
                physical_quantity=physical_quantity_list[k])
    item.save()
print("\n", Unit.objects.all())


# To populate PhysicalConstant
PhysicalConstant = models.PhysicalConstant
name_list = [
        "Earth's gravity",
]
value_list = [
        9.81,
]
unit_list = [
        models.Unit.objects.get(symbol="m/s^(-2)")
]
for k in range(0, len(name_list)):
    item = PhysicalConstant(
        name=name_list[k],
        value=value_list[k],
        unit=unit_list[k]
    )
    item.save()
print("\n", PhysicalConstant.objects.all())


# Energy type
EnergyType = models.EnergyType
delete_object(EnergyType.objects.all())
energy_type_list = ["thermal"]
for k in range(0, len(energy_type_list)):
    item = EnergyType(energy_type=energy_type_list[k])
    item.save()
print("\n", EnergyType.objects.all())


# Resource
Resource = models.Resource
delete_object(Resource.objects.all())
name_list = ["oil",
             "liquid petroleum gas (LPG)",
             "gasoline",
             "kerosene",
             "diesel",
            ]
weight_list = [1000,
               1000,
               1000,
               1000,
               1000,
              ]
weight_unit_list = [Unit.objects.get(symbol="kg"),
                    Unit.objects.get(symbol="kg"),
                    Unit.objects.get(symbol="kg"),
                    Unit.objects.get(symbol="kg"),
                    Unit.objects.get(symbol="kg"),
                   ]
volume_list = [1.165,
               1.844,
               1.328,
               1.253,
               1.186,
              ]
volume_unit_list = [Unit.objects.get(symbol="m^3"),
                    Unit.objects.get(symbol="m^3"),
                    Unit.objects.get(symbol="m^3"),
                    Unit.objects.get(symbol="m^3"),
                    Unit.objects.get(symbol="m^3"),
                   ]
density_list = [1000/1.165,
                1000/1.844,
                1000/1.328,
                1000/1.253,
                1000/1.186,
               ]
density_unit_list = [Unit.objects.get(symbol="kg/m^3"),
                     Unit.objects.get(symbol="kg/m^3"),
                     Unit.objects.get(symbol="kg/m^3"),
                     Unit.objects.get(symbol="kg/m^3"),
                     Unit.objects.get(symbol="kg/m^3"),
                    ]
density_ref_list = [
    Reference.objects.get(book="BP Statistical review of world energy"),
    Reference.objects.get(book="BP Statistical review of world energy"),
    Reference.objects.get(book="BP Statistical review of world energy"),
    Reference.objects.get(book="BP Statistical review of world energy"),
    Reference.objects.get(book="BP Statistical review of world energy"),
]

state_list = [PhysicalState.objects.get(state="liquid"),
              PhysicalState.objects.get(state="liquid"),
              PhysicalState.objects.get(state="liquid"),
              PhysicalState.objects.get(state="liquid"),
              PhysicalState.objects.get(state="liquid"),
             ]
price_list = [2,
              2,
              2,
              2,
              2,
             ]
for k in range(0,len(name_list)):
    item = Resource(name = name_list[k],
                    weight = weight_list[k],
                    weight_unit = weight_unit_list[k],
                    volume = volume_list[k],
                    volume_unit = volume_unit_list[k],
                    density = density_list[k],
                    density_unit = density_unit_list[k],
                    density_ref = density_ref_list[k],
                    state=state_list[k],
                    price=price_list[k])
    item.save()
print("\n", Resource.objects.all())


# Energy
# IMPORTANT : see the eia.gov https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php to see a conversion calculator
Energy = models.Energy
delete_object(Energy.objects.all())
resource_list = [Resource.objects.get(name="oil"),
                 Resource.objects.get(name="liquid petroleum gas (LPG)"),
                 Resource.objects.get(name="gasoline"),
                 Resource.objects.get(name="kerosene"),
                 Resource.objects.get(name="diesel"),
                ]
unit_list = [Unit.objects.get(unit="joule"),
             Unit.objects.get(unit="joule"),
             Unit.objects.get(unit="joule"),
             Unit.objects.get(unit="joule"),
             Unit.objects.get(unit="joule"),
            ]
#value_list = [42E9,
#              0.542*42E9,
#
#             ]
primary_list = [True,
                False,
                False,
                False,
                False,
               ]
final_list = [False,
              True,
              True,
              True,
              True,
             ]
# exemple J/m^3
energy_density_list = [
    37.859E9,
    27.7E9,
    33.539E9,
    38.346E9,
    38.290E9,
]
energy_density_unit_list = [Unit.objects.get(symbol="J/m^3"),
                            Unit.objects.get(symbol="J/m^3"),
                            Unit.objects.get(symbol="J/m^3"),
                            Unit.objects.get(symbol="J/m^3"),
                            Unit.objects.get(symbol="J/m^3"),
                           ]
energy_density_ref_list = [Reference.objects.all()[0],
                           Reference.objects.all()[2],
                           Reference.objects.all()[0],
                           Reference.objects.all()[3],
                           Reference.objects.all()[0],
                          ]
# exemple J/kg
specific_energy_list = [41.868E9,
                        49.1E9,
                        46.4E9,
                        46.2E9,
                        45.6E9,
                       ]
specific_energy_unit_list = [Unit.objects.get(symbol="J/kg"),
                             Unit.objects.get(symbol="J/kg"),
                             Unit.objects.get(symbol="J/kg"),
                             Unit.objects.get(symbol="J/kg"),
                             Unit.objects.get(symbol="J/kg"),
                            ]
specific_energy_ref_list = [Reference.objects.all()[2],
                            Reference.objects.all()[2],
                            Reference.objects.all()[2],
                            Reference.objects.all()[3],
                            Reference.objects.all()[2],
                           ]
energy_type_list = [EnergyType.objects.get(energy_type="thermal"),
                    EnergyType.objects.get(energy_type="thermal"),
                    EnergyType.objects.get(energy_type="thermal"),
                    EnergyType.objects.get(energy_type="thermal"),
                    EnergyType.objects.get(energy_type="thermal"),
                   ]
for k in range(0, len(resource_list)):
    item = Energy(resource=resource_list[k],
                  unit=unit_list[k],
#                  value=value_list[k],
                  primary=primary_list[k],
                  final=final_list[k],
                  energy_density=energy_density_list[k],
                  energy_density_unit=energy_density_unit_list[k],
                  energy_density_ref=energy_density_ref_list[k],
                  specific_energy=specific_energy_list[k],
                  specific_energy_unit=specific_energy_unit_list[k],
                  specific_energy_ref=specific_energy_ref_list[k],
                  energy_type=energy_type_list[k])
    item.save()
print("\n", Energy.objects.all())


## Power
#Power = models.Power
#delete_object(Power.objects.all())
#unit_list = [
#    Unit.objects.get(symbol="W"),
#]
##value_list = [1]
#for k in range(0, len(value_list)):
#    item = Power(
#        unit=unit_list[k],
##        value=value_list[k],
#    )
#    item.save()
#print("\n", Power.objects.all())


# Machine 
Machine = models.Machine
delete_object(Machine.objects.all())
name_list = ["car"]
resource_input_list = [Resource.objects.get(name="oil")]
resource_output_list = [Resource.objects.get(name="oil")]
energy_input_list = [Energy.objects.filter(resource__name__contains="oil")]
energy_output_list = [Energy.objects.filter(resource__name__contains="oil")]
efficiency_list = [0.3]
price_list = [10E3]
power_list = [75,
             ]
power_unit_list = [Unit.objects.get(symbol="ch"),
             ]
consumption_list = [6,]
consumption_unit_list = [
    Unit.objects.get(symbol="l/100km"),
]
for k in range(0, len(name_list)):
   item = Machine(name=name_list[k],
                  resource_input=resource_input_list[k],
                  resource_output=resource_input_list[k],
                  energy_input=energy_input_list[k][0],
                  energy_output=energy_output_list[k][0],
                  efficiency=efficiency_list[k],
                  price=price_list[k],
                  power=power_list[k],
                  power_unit=power_unit_list[k],
                  consumption=consumption_list[k],
                  consumption_unit=consumption_unit_list[k],
                 )
   item.save()
print("\n", Machine.objects.all())


# To populate the Human class
Human = models.Human
delete_object(Human.objects.all())
power_unit = models.Unit.objects.get(symbol="W")
weight_unit = models.Unit.objects.get(symbol="kg")
human = Human(arms_power=10,
              arms_power_unit=power_unit,
              legs_power=100,
              legs_power_unit=power_unit,
              weight=100,
              weight_unit=weight_unit)
human.save()
print("\n", Human.objects.all())


# To populate HeightScale
HeightScale = models.HeightScale
delete_object(HeightScale.objects.all())
name_list = ["Tour Eiffel"]
height_list = [324]
height_unit_list = [
    models.Unit.objects.get(symbol="m"),
]
for k in range(0, len(name_list)):
    item = HeightScale(name=name_list[k],
                       height=height_list[k],
                       height_unit=height_unit_list[k])
    item.save()
print("\n", HeightScale.objects.all())


# To populate ConversonCoefficient
ConversionCoefficient = models.ConversionCoefficient
delete_object(ConversionCoefficient.objects.all())
unit_from_list = [
    models.Unit.objects.get(symbol="W"),
    models.Unit.objects.get(symbol="ch"),
    models.Unit.objects.get(symbol="kW"),
    models.Unit.objects.get(symbol="h"),
    models.Unit.objects.get(symbol="m"),
    models.Unit.objects.get(symbol="km"),
    models.Unit.objects.get(symbol="km"),
    models.Unit.objects.get(symbol="l/100km"),
    models.Unit.objects.get(symbol="m^3"),
    models.Unit.objects.get(symbol="l"),
    models.Unit.objects.get(symbol="J"),
]
unit_to_list = [
    models.Unit.objects.get(symbol="W"),
    models.Unit.objects.get(symbol="W"),
    models.Unit.objects.get(symbol="W"),
    models.Unit.objects.get(symbol="s"),
    models.Unit.objects.get(symbol="m"),
    models.Unit.objects.get(symbol="km"),
    models.Unit.objects.get(symbol="m"),
    models.Unit.objects.get(symbol="l/100km"),
    models.Unit.objects.get(symbol="l"),
    models.Unit.objects.get(symbol="m^3"),
    models.Unit.objects.get(symbol="J"),
]
value_list = [
    1,
    735.5,
    1000,
    3600,
    1,
    1,
    1000,
    1,
    1000,
    1/1000,
    1,
]
for k in range(0, len(unit_from_list)):
    item = ConversionCoefficient(unit_from=unit_from_list[k],
                                 unit_to=unit_to_list[k],
                                 value=value_list[k])
    item.save()
print("\n", ConversionCoefficient.objects.all())

from django.db import models
"""
To do :
indiquer la devise du prix
Déterminer une structure pour les références.
    faire une classe abstract pour référence et
    faire hérité cette classe au URL ou book.
"""

class Reference(models.Model):
    url = models.CharField(max_length=200, null=True)
    # see later if I have to make a book table
    book = models.CharField(max_length=200, null=True)
    def __def__(self):
        return "{}".format("URL : {} | book : {}".format(self.url, self.book))
    def __str__(self):
        return self.__def__()


class PhysicalState(models.Model):
    """
    Such as solid, liquid, gas
    """
    state = models.CharField(max_length=100, default="solid")
    def __def__(self):
        return "{}".format(self.state)
    def __str__(self):
        return self.__def__()


class PhysicalQuantity(models.Model):
    """
    Exemple : Energy, Mass, Volume,
    Temperature, Specific volume...
    """
    physical_quantity = models.CharField(max_length=100, default="DEFAULT")
    def __def__(self):
        return self.physical_quantity
    def __str__(self):
        return self.__def__()


class Unit(models.Model):
    unit = models.CharField(max_length=100, default="DEFAULT")
    symbol = models.CharField(max_length=100, default="DEFAULT")
    comment = models.TextField(null=True, blank=True)
    physical_quantity = models.ForeignKey('PhysicalQuantity',
                                          null=False,
                                          on_delete=models.CASCADE,)
    class Meta:
        ordering = ['symbol']
    def __def__(self):
        return self.symbol
    def __str__(self):
        return self.__def__()


class PhysicalConstant(models.Model):
    name = models.CharField(max_length=100, null=True)
    value = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    unit = models.ForeignKey('Unit', null=False, on_delete=models.CASCADE)
    def __def__(self):
        return "{} : {} {}".format(self.name, self.value, self.unit)
    def __str__(self):
        return self.__def__()


class EnergyType(models.Model):
    energy_type = models.CharField(max_length=100, default="thermal")
    def __def__(self):
        return self.energy_type
    def __str__(self):
        return self.__def__()


class Resource(models.Model):
    name = models.CharField(max_length=100, default="resource")
    weight = models.DecimalField(max_digits=19,
                                 decimal_places=10,
                                 null=True,
                                 default=0)
    weight_unit = models.ForeignKey('Unit',
                                    null=False,
                                    on_delete=models.CASCADE,
                                    related_name='Resource_weight_unit')
    volume = models.DecimalField(max_digits=19,
                                 decimal_places=10,
                                 null=True,
                                 default=0)
    volume_unit = models.ForeignKey('Unit',
                                    null=False,
                                    on_delete=models.CASCADE,
                                    related_name='Resource_volume_unit')
    density = models.DecimalField(max_digits=19,
                                  decimal_places=10,
                                  default=0)
    density_unit = models.ForeignKey('Unit',
                                     null=False,
                                     on_delete=models.CASCADE,
                                     related_name='Resource_density_unit')
    density_ref = models.ForeignKey('Reference',
                                    null=True,
                                    on_delete=models.CASCADE,
                                    related_name="density_ref")
    state = models.ForeignKey('PhysicalState',
                              null=False,
                              on_delete=models.CASCADE)
    #Le prix est le prix global ou au poids ?
    price = models.DecimalField(max_digits=19,
                                decimal_places=10,
                                default=0)
    price_ref = models.ForeignKey('Reference',
                                  null=True,
                                  on_delete=models.CASCADE,
                                  related_name="price_ref")
    class Meta:
        ordering = ['name']
    def __def__(self):
        return self.name
    def __str__(self):
        return self.__def__()


class Energy(models.Model):
    resource = models.ForeignKey('Resource',
                                 null=True,
                                 on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit',
                             null=False,
                             on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=21,
                                decimal_places=3,
                                default=0,
                                null=True)
    primary = models.BooleanField(default="True")
    final = models.BooleanField(default="False")
    # exemple J/m^3
    energy_density = models.DecimalField(max_digits=21,
                                         decimal_places=10,
                                         default=0,
                                         null=True)
    # exemple J/m^3
    energy_density_unit = models.ForeignKey("Unit",
                                            null=False,
                                            on_delete=models.CASCADE,
                                            related_name="energy_density_unit")
    energy_density_ref = models.ForeignKey('Reference',
                                           null=True,
                                           on_delete=models.CASCADE,
                                           related_name="energy_density_ref")
    # exemple : J/kg
    specific_energy = models.DecimalField(max_digits=30,
                                         decimal_places=15,
                                         default=0,
                                         null=True)
    # exemple : J/kg
    specific_energy_unit = models.ForeignKey("Unit",
                                            null=False,
                                            on_delete=models.CASCADE,
                                            related_name="specific_energy_unit")
    specific_energy_ref = models.ForeignKey('Reference',
                                            null=True,
                                            on_delete=models.CASCADE,
                                            related_name="specific_energy_ref")
    energy_type = models.ForeignKey('EnergyType',
                                    null=False,
                                    on_delete=models.CASCADE)
    class Meta:
        ordering = ['resource']
    def __def__(self):
        return "{} : {} {}".format(self.resource, self.value, self.unit.symbol)
    def __str__(self):
        return self.__def__()


#class Power(models.Model):
##    # A voir si je garde l'attribut resource
##    resource = models.ForeignKey('Resource',
##                                 null=True,
##                                 on_delete=models.CASCADE,
##                                 default="J")
#    unit = models.ForeignKey('Unit',
#                             null=False,
#                             on_delete=models.CASCADE,
#                             default="W")
#    value = models.DecimalField(max_digits=19,
#                                decimal_places=10,
#                                null=True,
#                                default=0)
#    def __def__(self):
#        return "{} {}".format(self.value, self.unit.symbol)
#    def __str__(self):
#        return self.__def__()


class Machine(models.Model):
    name = models.CharField(max_length=100)
    resource_input = models.ForeignKey('Resource',
                                       null=True,
                                       on_delete=models.CASCADE,
                                       related_name="Machine_resource_input")
    resource_output = models.ForeignKey('Resource',
                                        null=True,
                                        on_delete=models.CASCADE,
                                        related_name="Machine_resource_output")
    energy_input = models.ForeignKey('Energy',
                                     null=True,
                                     on_delete=models.CASCADE,
                                     related_name="Machine_energy_input")
    energy_output = models.ForeignKey('Energy',
                                      null=True,
                                      on_delete=models.CASCADE,
                                      related_name="Machine_energy_output")
    efficiency = models.DecimalField(max_digits=19,
                                     decimal_places=10,
                                     default=0)
    price = models.DecimalField(max_digits=19,
                                decimal_places=10,
                                default=0)
    power = models.DecimalField(max_digits=19,
                                decimal_places=10,
                                default=0)
    power_unit = models.ForeignKey('Unit',
                              null=True,
                              on_delete=models.CASCADE,
#                              related_name="%(app_label)s_%(class)s_related")
                              related_name="+")
    consumption = models.DecimalField(max_digits=19,
                                decimal_places=10,
                                default=0)
    consumption_unit = models.ForeignKey('Unit',
                              null=True,
                              on_delete=models.CASCADE,
#                              related_name="%(app_label)s_%(class)s_related")
                              related_name="+")
    def __def__(self):
        return self.name
    def __str__(self):
        return self.__def__()

class Human(models.Model):
    arms_power = models.DecimalField(max_digits=4,
                                     decimal_places=0,
                                     null=True)
    arms_power_unit = models.ForeignKey('Unit',
                                        null=False,
                                        on_delete=models.CASCADE,
                                        related_name="Human_arms_power_unit")
    legs_power = models.DecimalField(max_digits=4,
                                     decimal_places=0,
                                     null=True)
    legs_power_unit = models.ForeignKey('Unit',
                                        null=False,
                                        on_delete=models.CASCADE,
                                        related_name="Human_legs_power_unit")
    weight = models.DecimalField(max_digits=4,
                                 decimal_places=0,
                                 null=True)
    weight_unit = models.ForeignKey('Unit',
                                    null=False,
                                    on_delete=models.CASCADE,
                                    related_name="Human_weight_unit")
    def __def__(self):
        return ("arms's power : {} {} and legs's power : {} {}"
                .format(self.arms_power,
                        self.arms_power_unit,
                        self.legs_power,
                        self.legs_power_unit))
    def __str__(self):
        return self.__def__()


class HeightScale(models.Model):
    name = models.CharField(max_length=100,
                            null=True)
    height = models.DecimalField(max_digits=4,
                                 decimal_places=0,
                                 null=True)
    height_unit = models.ForeignKey('Unit',
                                    null=False,
                                    on_delete=models.CASCADE,
                                    related_name="HeightScale_height_unit")
    def __def__(self):
        return ("{} : {} {}".format(self.name,
                                    self.height,
                                    self.height_unit))
    def __str__(self):
        return self.__def__()

## Try to make a model that will automatise
## the form for scale.html
#class Test(models.mOdel):
#    energy = models.ForeignKey('Energy')
#    unit = forms.ChoiceField(widget=forms.RadioSelect)
#    value = forms.FloatField()
#    name = forms.ChoiceField(widget=forms.RadioSelect)
#    def __def__(self):
#        return ("{} : {} {}".format(self.name,
#                                    self.height,
#                                    self.height_unit))
#    def __str__(self):
#        return self.__def__()

class ConversionCoefficient(models.Model):
    unit_from = models.ForeignKey('Unit',
                              null=True,
                              on_delete=models.CASCADE,
#                              related_name="%(app_label)s_%(class)s_related")
                              related_name="+")
    unit_to = models.ForeignKey('Unit',
                              null=True,
                              on_delete=models.CASCADE,
#                              related_name="%(app_label)s_%(class)s_related")
                              related_name="+")
    value = models.DecimalField(max_digits=21,
                                decimal_places=3,
                                default=0,
                                null=True)
    def __def__(self):
        return ("{} = {} {}".format(self.unit_from,
                                    self.value,
                                    self.unit_to))
    def __str__(self):
        return self.__def__()

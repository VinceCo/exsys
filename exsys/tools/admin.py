from django.contrib import admin
from tools import models


#class PhysicalStateAdmin(admin.ModelAdmin):
#    list_display = ('state',)
#    list_filter = ('state',)
#
#
#class PhysicalQuantityAdmin(admin.ModelAdmin):
#    list_display = ('physical_quantity',)
#    list_filter = ('physical_quantity',)
#
#
#class UnitAdmin(admin.ModelAdmin):
#    list_display = ('unit','symbol', 'comment')
#    list_filter = ('unit','symbol', 'comment')
#
#
#class EnergyTypeAdmin(admin.ModelAdmin):
#    list_display = ('energy_type',)
#    list_filter= ('energy_type',)
#
#
#class ResourceAdmin(admin.ModelAdmin):
#    list_display = ('name','weight', 'weight_unit',
#                    'volume', 'volume_unit',
#                    'density', 'density_unit',
#                    'state', 'price')
#    list_filter = ('name','weight', 'weight_unit',
#                    'volume', 'volume_unit',
#                    'density', 'density_unit',
#                    'state', 'price')
#
#
#class EnergyAdmin(admin.ModelAdmin):
#    list_display = ('unit', 'value',)
#    list_filter = ('unit', 'value',)
#
#
#class PowerAdmin(admin.ModelAdmin):
#    list_display = ('unit', 'value',)
#    list_filter = ('unit', 'value',)
#
#
##class MachineAdmin(admin.ModelAdmin):
##    list_display = ('name',
##                    'resource_input',
##                    'resource_output',
##                    'energy_input',
##                    'energy_output',
##                    'efficiency',
##                    'price',)
##    list_filter = ('name',
##                   'resource_input',
##                   'resource_output',
##                   'energy_input',
##                   'energy_output',
##                   'efficiency',
##                   'price',)
##
#
#admin.site.register(models.PhysicalState, PhysicalStateAdmin)
#admin.site.register(models.PhysicalQuantity, PhysicalQuantityAdmin)
#admin.site.register(models.Unit, UnitAdmin)
#admin.site.register(models.EnergyType, EnergyTypeAdmin)
#admin.site.register(models.Resource, ResourceAdmin)
#admin.site.register(models.Energy, EnergyAdmin)
#admin.site.register(models.Power, PowerAdmin)
##admin.site.register(models.Machine, MachineAdmin)

from django.contrib import admin
from models.models import  Report
from models.models import  ReportItem
from models.models import  ReportText
from models.models import  Figure


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('title','date')


class ReportItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'report', 'item_nb')
    list_filter = ('title','date','report', 'item_nb')


class ReportTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'text', 'report', 'item_nb')
    list_filter = ('title','date','report', 'item_nb')


class FigureAdmin(admin.ModelAdmin):
    list_display = ('title', 'fig', 'date', 'report', 'item_nb')
    list_filter = ('title','date','report', 'item_nb')


admin.site.register(Report, ReportAdmin)
admin.site.register(ReportItem, ReportItemAdmin)
admin.site.register(ReportText, ReportTextAdmin)
admin.site.register(Figure, FigureAdmin)

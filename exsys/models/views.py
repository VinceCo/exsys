from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from models.models import Report
from models.models import ReportItem
from models.models import ReportText
from models.models import Figure

def home(request):
    reports = Report.objects.all()
    return render(request, 'models/home.html', locals())

def redirect_home(request):
    return redirect('home')

def model(request, id_title):
    report = Report.objects.get(title=id_title)
    report_items = report.reportitem_set.all()
    report_texts = ReportText.objects.filter(report__title=report.title)
    figures = Figure.objects.filter(report__title=report.title)
    item_list = []

    # This block is sorting texts and figures
    for k in range(0, len(report_items)):
        q_item_text = report_texts.filter(item_nb=k)
        q_item_figure = figures.filter(item_nb=k)
        if q_item_text.exists():
            item_list.append(q_item_text[0])
        if q_item_figure.exists():
            item_list.append(q_item_figure[0])

#    items = [report_texts[k] for k in range(0, len(report_texts))]
#    for fig in figures:
#        items.append(fig)


    # They must be a better way to have access to
    # reporttext and figures
#    for item in report_items:
#        try:
#            if item.reporttext is not None:
#                item_list.append(item.reporttext)
#        except:
#            try:
#                if item.figure is not None:
#                    item_list.append(item.figure)
#            except:
#                pass
    return render(request, 'models/model.html', locals())

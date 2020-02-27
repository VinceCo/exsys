from django.db import models
from blog import models as blog_models

class Report(blog_models.ItemCommonInfo):
    pass


class ReportItem(blog_models.Item):
    report = models.ForeignKey('report', null=True, on_delete=models.CASCADE,)
    item_nb = models.PositiveIntegerField(unique=True)


class ReportText(ReportItem):
    text = models.TextField(blank=False, null=True)


class Figure(ReportItem):
    fig = models.ImageField(upload_to="models/")

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
##        return reverse('sketches')
#        return reverse('figures')

from django.db import models
from blog import models as blog_models

class Report(blog_models.ItemCommonInfo):
    subjet = models.CharField(max_length=100, default='Subjet')


class ReportText(blog_models.ItemCommonInfo):
    text = models.ForeignKey('report', null=True, on_delete=models.CASCADE,)


class Graphic(models.Model):
    graphic = models.ImageField(upload_to="models/")
    title = models.CharField(max_length=100, default='Item')

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
#        return reverse('sketches')

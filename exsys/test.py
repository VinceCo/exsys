# forms.py
# https://docs.djangoproject.com/en/2.2/ref/forms/api/
# https://stackoverflow.com/questions/657607/setting-the-selected-value-on-a-django-forms-choicefield

class TestForm(forms.Form):
    radio = forms.ChoiceField(widget=forms.RadioSelect)

# https://docs.djangoproject.com/en/2.2/ref/forms/widgets/#widgets-inheriting-from-the-select-widget
# Dans la vue, pour initialiser le formulaire
def test(request):
    CHOICES = [('1', 'First'), ('2', 'Second')]
    form = forms.TestForm()
    form.radio(choices=CHOICES)
    return render(request, 'scale/test.html', locals())

# Autre manière de faire
def test(request):
    CHOICES = [('1', 'First'), ('2', 'Second')]
    form = forms.TestForm()
    form.radio = CHOICES
    return render(request, 'scale/test.html', locals())


#######
# Autre manière de faire
# forms.py
CHOICES = [('1', 'First'), ('2', 'Second')]
class TestForm(forms.Form):
    radio = forms.ChoiceField(widget=forms.RadioSelect, 
        choices=CHOICES)


def test(request):
    form = forms.TestForm()
    return render(request, 'scale/test.html', locals())
# Si cela fonctionne, il faut que je construise les choix possibles
# avec l'aide des données issues des bdd.


#######
# Autre manière
class TestForm(forms.Form):
    radio = forms.ChoiceField(widget=formsRadioSelect)

def test(request):
    TestFormSet = formset_factory(forms.TestForm)
    formset = TestFormSet(initial={
        'radio': [('1', 'First'), ('2', 'Second')]})
    return render(request, 'scale/test.html', locals())

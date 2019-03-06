from django import forms
from .models import Portfolio

class PortfolioPost(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields =['title','image','description']
    '''
    title = forms.CharField()
    image = forms.FileField()
    description = forms.CharField()
    '''
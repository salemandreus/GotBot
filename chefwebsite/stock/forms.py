from django import forms

from .models import Stock

class StockForm(forms.Form):
    amount = forms.IntegerField()

class StockModelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['amount']

from django import forms

class FoodForm(forms.Form):
    food = forms.CharField(label='好きなフード', max_length=100)
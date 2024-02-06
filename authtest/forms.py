# forms.py

from django import forms

FLAVOR_CHOICES = [
    ('citrus', 'シトラス系'),
    ('chocolate', 'チョコレート系'),
    ('spice', 'スパイス系'),
    ('fruit', 'フルーツ系'),
    ('nuts', 'ナッツ系'),
    ('other', 'その他'),
]

class FlavorForm(forms.Form):
    flavor = forms.MultipleChoiceField(
        choices=FLAVOR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='フレーバー'
    )
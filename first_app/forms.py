from django import forms
from django.forms.widgets import NumberInput
import datetime
class practice(forms.Form):
    name=forms.CharField(initial='Your name',widget=forms.Textarea(attrs={'rows':3}))
    email=forms.EmailField(label="Please enter your email address",required = False,)
    text=forms.CharField(widget=forms.Textarea,max_length = 10,)
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    time = forms.TimeField()
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    favoritecolorss = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)


    
   
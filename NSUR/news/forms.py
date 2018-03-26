from django import forms
from . import models

class Email(forms.Form):
    name = forms.CharField()
    tel = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    sendBack = forms.BooleanField()

    class Meta:
        model = models.EmailUs
        fields = ['name','tel','email','text','sendBack']

class EmailFooter(forms.Form):
    nameFooter = forms.CharField()
    emailFooter = forms.EmailField()
    textFooter = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.EmailUs
        fields = ['nameFooter','emailFooter','textFooter']
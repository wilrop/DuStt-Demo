from django import forms

class AudioFile(forms.Form):
    file = forms.FileField()
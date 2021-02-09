from django import forms


class UploadForm(forms.Form):
    uploadFile = forms.FileField()
    convertFormat = forms.CharField()

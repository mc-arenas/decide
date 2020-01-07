from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class NewVotingForm(forms.Form):
    name = forms.TextInput()
    description = forms.Textarea()
    candidatures = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    candidature_name = forms.TextInput()
    candidature_file = forms.FileField()
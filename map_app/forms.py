from django import forms


class UploadGPXForm(forms.Form):
    gpx_file = forms.FileField(max_length=100, required=False, help_text='Upload geometry by GPX file')

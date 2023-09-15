from django import forms
from django.core import validators


def check_for_z_start(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("name must start with z !")


class UserInputForm(forms.Form):
    name = forms.CharField(validators=[check_for_z_start])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # custom validator : starts with 'clean_<field_name>'
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Got you Bot")
    #     return botcatcher

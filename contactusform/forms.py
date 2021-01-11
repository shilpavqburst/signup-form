from django import forms
from .models import Contactusform


class Contactform(forms.ModelForm):
    name = forms.CharField(label='Name:', required=False, min_length=3, max_length=100)
    email = forms.EmailField(label='Email:', required=False)
    phone_no = forms.CharField(label='Phone No:',required=False, widget=forms.TextInput)
    description = forms.CharField(label='Description:',required=False, widget=forms.Textarea)

    class Meta:
        model = Contactusform
        fields = ('id','name','email','phone_no','description')

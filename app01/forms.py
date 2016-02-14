__author__ = 'Yang'

from django import forms

# 1.To generate html
# 2.To verify user's input

class Login(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    ip = forms.GenericIPAddressField()


# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False, label='Your e-mail address')
#     message = forms.CharField(widget=forms.Textarea)

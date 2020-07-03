from django import forms
from twitteruser.models import TwitterUser

# log_in
class create_user(forms.Form):
    name = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class log_in(forms.Form):
    name = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput, label='Password again')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def is_valid(self):
        valid = super(UserForm, self).is_valid()
        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            self.add_error('password_repeat', 'passwords should be equal')
            valid = False
        return valid


class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

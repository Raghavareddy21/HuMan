from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
Types=(('V', 'Vegitarian'),('N', 'NonVegitarian'))
class DonateFood(forms.ModelForm):
    Type = forms.ChoiceField(choices=Types, widget=forms.RadioSelect())
    class Meta:
        model=models.FoodDiscription
        fields=('name','cooking_date','expiry_date','Type','quantity')
class Register(forms.Form):
    first_name = forms.CharField(label='First name',max_length=20, required=False, help_text='optional')
    last_name = forms.CharField(label='Last name',max_length=20, required=False, help_text='optional')
    username = forms.CharField(label='Username',max_length=40, required=True)
    password1 = forms.CharField(label='Password',max_length=30, required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',max_length=30, required=True,widget=forms.PasswordInput)
    phone=forms.IntegerField(label='Phone Number',required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'password1', 'password2', 'phone' )
    def clean_username(self):
        user = self.cleaned_data.get('username').lower()
        check = User.objects.filter(username=user)
        if check.count() > 0:
            raise forms.ValidationError(' The username is already in use please choose different one')
        else:
            return user
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Please enter same passwords both the times')
        if not(password1) and not(password2):
            raise forms.ValidationError('Please fill the password fields')
        if len(password1) < 8:
            raise forms.ValidationError('The password must be atleast 8 characters')
        return True
    def save(self):
        user = User.objects.create_user(
        username=self.cleaned_data.get('username'),
        password=self.cleaned_data.get('password1'),
        first_name=self.cleaned_data.get('first_name'),
        last_name=self.cleaned_data.get('last_name')
        )

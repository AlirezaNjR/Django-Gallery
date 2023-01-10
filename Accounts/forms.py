from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm , UserCreationForm 
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('avatar','location','gender','age')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=50,required=True,label=' نام کاربری')
    name = forms.CharField(max_length=50,required=True,label=' نام')
    family = forms.CharField(max_length=50,required=True,label=' نام خانوادگی')
    email = forms.EmailField(max_length=255, required=False,label='ایمیل ',)
    location = forms.ChoiceField(choices=CustomUser.LOCATIONS, required=False,label=' مکان')
    sex = forms.ChoiceField(choices=CustomUser.GENDER,required=False,label=' جنسیت')
    avatar = forms.ImageField(required=False,label='تصویر پروفایل')
    age = forms.IntegerField(max_value=120,min_value=0,required=False,label=' سن')
    password = forms.CharField(widget=forms.PasswordInput,required=True,max_length=255,label='رمز عبور ')
    check_password = forms.CharField(widget=forms.PasswordInput,required=True,max_length=255,label=' تایید رمز عبور')
    
    def clean_check_password(self):
        password = self.cleaned_data['password']
        c_password = self.cleaned_data['check_password']
        if password != c_password:
            raise forms.ValidationError('رمز عبور ها مطابقت ندارد')
        elif len(password) < 8 :
            raise forms.ValidationError('رمز عبور کوتاه است')
        else :
            return c_password
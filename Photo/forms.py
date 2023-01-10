from django import forms
from .models import  Photo

class AddPicForm(forms.Form):
    
    LOCATIONS = (
    ('ایران','ایران'),
    ('آمریکا','آمریکا'),
    ('ترکیه','ترکیه'),
    ('روسیه','روسیه'),
    ('کره','کره'),
    )
    title  = forms.CharField(required=True,max_length=250,label='عنوان')
    body = forms.CharField(widget=forms.Textarea,required=False,label='توضیحات')
    image = forms.ImageField(required=False,label='تصویر')
    location = forms.ChoiceField(choices=LOCATIONS,label='مکان')
    tags = forms.CharField(max_length=500, required=True,label='تگ ها')
    
class ChangePicForm(forms.Form): 
    
    LOCATIONS = (
    ('ایران','ایران'),
    ('آمریکا','آمریکا'),
    ('ترکیه','ترکیه'),
    ('روسیه','روسیه'),
    ('کره','کره'),
    )
    
    title  = forms.CharField(required=False,max_length=250,label='عنوان')
    body = forms.CharField(widget=forms.Textarea,required=False,label='توضیحات')
    image = forms.ImageField(required=False,label='تصویر')
    location = forms.ChoiceField(choices=LOCATIONS,label='مکان',required=False)
    tags = forms.CharField(max_length=500, required=True,label='تگ ها')
    
    def clean_title(self):
        text = self.cleaned_data['title']
        if not text:
            raise forms.ValidationError(' نمیتواند خالی باشد')
        else:
            return text
    
    def clean_body(self):
        text = self.cleaned_data['body']
        if not text:
            raise forms.ValidationError('نمیتواند خالی باشد')
        else:
            return text

    def clean_tags(self):
        text = self.cleaned_data['tags']
        if text:
            if ('@'in text) or ('$' in text) or ('.'in text) or ('/' in text) or ('\\' in text):
                raise forms.ValidationError('نمیتوان از (@  $  %  /  .  \\ )استفاده کرد')
            else:
                return text
        else:
            raise forms.ValidationError('نمیتواند خالی باشد')
        
class CommentForm(forms.Form):
    name = forms.CharField(max_length=50,required=True,label='* نام و نام خانوادگی')
    email = forms.EmailField(max_length=200, required=True,label='* ایمیل')
    body = forms.CharField(widget=forms.Textarea,max_length=500,required=True,label='* متن')
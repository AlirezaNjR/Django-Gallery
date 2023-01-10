from .models import CustomUser
from Photo.models import Photo
from django.shortcuts import render , redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate
# Create your views here.
    
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST,request.FILES)
        if form.is_valid():
            user = CustomUser()
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['family']
            user.email = form.cleaned_data['email']
            user.age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            check_password = form.cleaned_data['check_password']
            if password == check_password:
                if len(password) >= 8:
                    user.set_password(password)
                    user.save()
                    return redirect('Gallery:Home')
            else:
                pass
        else:
            pass
    else:
        form = CreateUserForm()
    return render(request,'registration/create_user.html',{'form':form})
    
def user_info(request,pk):
    user = CustomUser.objects.get(id=pk)
    last_photo = Photo.objects.filter(photo_grapher=user).order_by('-date')[0:10]
    return render(request,'registration/user_profile.html',{'User':user,'Last_Photo':last_photo})

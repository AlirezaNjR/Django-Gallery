from django.shortcuts import render

def contact_me(request):
    return render(request,'main/contact_me.html')

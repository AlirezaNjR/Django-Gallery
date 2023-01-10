from django.urls import path
from .views import user_info , create_user

app_name = 'Accounts'

urlpatterns = [
    path('accounts/<int:pk>/Profile/',user_info,name='Profile'),
    path('accounts/Create/',create_user,name='Create_user'),
    
]
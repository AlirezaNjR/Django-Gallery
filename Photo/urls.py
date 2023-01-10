from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import * #HomePageView , DeletePicView , CreateUserView  ,  UserInfoView , AddNewPicView , Search

app_name = 'Gallery'

urlpatterns = [
    path('',home_page,name="Home"),
    path('Tag/<slug:tag>',home_page,name="Tag"),
    path('search/',search,name='Search'),
    path('Add-Pic/',add_pic,name="Add_Pic"),
    path('<int:pk>/Detail/',photo_detail,name='Detail'),
    path('<int:pk>/Change/',change_pic,name='Change'),
    path('<int:pk>/Delete/',DeletePicView.as_view(),name='Delete'),

] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
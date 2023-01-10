from .models import Photo 
from taggit.models import Tag
from django.urls import reverse_lazy
from django.shortcuts import render , redirect
from django.views.generic.edit import DeleteView 
from comments.models import CommentModel
from django.views.generic import DetailView 
from django.contrib.auth.decorators import login_required
from .forms import AddPicForm , ChangePicForm , CommentForm
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


def home_page(request,tag=None):
    if tag:
        tags = Tag.objects.get(slug=tag)
        photos = Photo.objects.filter(tags__in=[tags])
        paginator = Paginator(photos,6)
    else:
        photos = Photo.objects.all().order_by('-date')
        paginator = Paginator(photos,6)
        
    page = request.GET.get('page')

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    context = {
        'Gallery':photos ,
        'search_word':tag ,
        'page':page,
    }
    return render(request,'index.html',context)

class DeletePicView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,DetailView):
    model = Photo
    template_name = 'photo/delete_Pic.html'
    success_url = reverse_lazy('Gallery:Home')
    context_object_name = "Pic"
    
    def test_func(self):
        obj = self.get_object()
        return obj.photo_grapher == self.request.user

@login_required(login_url='login')
def add_pic(request):
    if request.method == "POST":
        form = AddPicForm(request.POST,request.FILES)
        if form.is_valid():
            new_pic = Photo()
            new_pic.title = form.cleaned_data['title']
            new_pic.body = form.cleaned_data['body']
            new_pic.location = form.cleaned_data['location']
            new_pic.photo_grapher = request.user
            new_pic.image = request.FILES['image']
            new_pic.save()
            tags = form.cleaned_data['tags']
            tags = tags.split(',')
            for tag in tags:
                tag = tag.strip()
                new_pic.tags.add(tag)
            return redirect('Gallery:Home')
        else:
            pass
    else:
        form = AddPicForm()
    return render(request,'photo/add_pic.html',{'form':form})

def photo_detail(request,pk):
    photo = Photo.objects.get(id=pk)
    tags = photo.tags.all()
    comments = photo.comment.all()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = CommentModel()
            comment.name = form.cleaned_data['name']
            comment.body = form.cleaned_data['body']
            comment.email = form.cleaned_data['email']
            comment.photo = photo
            comment.save()
        else:
            pass
    else:
        form = CommentForm()
    return render(request,'photo/detail.html',{'Photo':photo,'form':form,"comments":comments,'tags':tags})

def change_pic(request,pk):
    photo = Photo.objects.get(id=pk)
    tags = photo.tags.all()
    if request.method == "POST":
        form = ChangePicForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            photo.title = form.cleaned_data['title']
            photo.body = form.cleaned_data['body']
            photo.location = form.cleaned_data['location']
            
            photo.tags.clear()
            tagss = form.cleaned_data['tags']
            tagss = tagss.split(',')
            for tag in tagss :
                tag = tag.strip()   
                if tag in photo.tags.all():
                    pass
                if tag not in photo.tags.all():
                    photo.tags.add(tag)
                    
            if (request.FILES != {}) and (form.cleaned_data['image'] == None):
                photo.image = request.FILES['image']
                photo.save()
            else:
                photo.save()
                
            return redirect(photo.get_absolute_url())
        else:
            pass
    else:
        form = ChangePicForm()
    return render(request,'photo/change.html',{'Photo':photo,'form':form,'tags':tags})




def search(request):
    if request.method == "POST":
        query_name = request.POST.get('search')
        tag = Tag.objects.filter(slug=query_name)
        photos = Photo.objects.filter(title__contains=query_name) or Photo.objects.filter(body__contains=query_name) or \
        Photo.objects.filter(location=query_name) or Photo.objects.filter(tags__in=tag)
    return render(request,'index.html',{'Gallery':photos,'search_word':query_name})


from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.db.models import F
from .models import Image, Profile, Comments, Followers, PhotoLikes
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, EditProfile,CommentForm,Likes,FollowForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user=request.user.id
    images = Image.all_images()
    profile_image=Profile.objects.filter(id=current_user)
    profile=profile_image.reverse()[0:1]
    comments=Comments.objects.all()
    users=User.objects.all().exclude(id=request.user.id)
    row = round(len(images)/4)
    return render(request, 'home.html', {"images": images,"profile":profile,"users":users,"comments":comments})
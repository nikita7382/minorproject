from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib import messages
from .models import Movie
from django.http import HttpResponse #new
from . poster_api import fetch_poster,fetch_overview
import numpy as np

import pandas
import pickle
import os
filepath ='C:\\Users\Dell\Desktop\popular.pkl'
if os.path.exists(filepath):
    file = open('C:\\Users\Dell\Desktop\popular.pkl', 'rb')
    popular_df= pickle.load(file)
    file.close()
else:
    print("File not present at desired location")


filepath ='C:\\Users\Dell\Desktop\pt.pkl'
if os.path.exists(filepath):
    file = open('C:\\Users\Dell\Desktop\pt.pkl', 'rb')
    pt= pickle.load(file)
    file.close()
else:
    print("File not present at desired location")

filepath ='C:\\Users\Dell\Desktop\movier.pkl'
if os.path.exists(filepath):
    file = open('C:\\Users\Dell\Desktop\movier.pkl', 'rb')
    movier= pickle.load(file)
    file.close()
else:
    print("File not present at desired location")

filepath ='C:\\Users\Dell\Desktop\similarity_scores.pkl'
if os.path.exists(filepath):
    file = open('C:\\Users\Dell\Desktop\similarity_scores.pkl', 'rb')
    similarity_scores= pickle.load(file)
    file.close()
else:
    print("File not present at desired location")



# Create your views here.



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=UserCreationForm()
    print()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Error has occured!')

    context={'form':form}
    return render(request,'app/register.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            print(username)
            password=request.POST.get('password')
            print(password)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Credential Invalid")


    return render(request,'app/login.html')

def home(request):
    # movie=Movie.objects.filter(movie_id=285)
    # print(movie)
    image=[]
    overview=[]
    movie_id=list(popular_df['tmdbId'])[0:15]
    for i in movie_id:
        # print(fetch_poster(i))
        image.append(fetch_poster(i))
        overview.append(fetch_overview(i))
        
    
    print(overview)
    print(image)
    context={'movie_name':list(popular_df['title'])[0:15],'images':image,'overview':overview,'genres':list(popular_df['genres'])[0:15],'votes':list(popular_df['num_ratings'])[0:15],'rating':list(popular_df['avg_rating'])[0:15]}
    print(context)
    return render(request, 'app/index.html',context)

# @login_required(login_url='loginRegister')
def logoutUser(request):
    logout(request)
    return redirect('login.html')


def my_list(request):
    return render(request, 'app/mylist.html')


def recommend(request):
    context={}
    if request.method=='POST':
        user_input=request.POST['input']
        print(user_input)
        if input:
            index=np.where(pt.index==user_input)[0][0]
            similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
            images=[]
            data=[]
            for i in similar_items:
                item=[]
                temp_df=movier[movier['title']==pt.index[i[0]]]
                item.extend(list(temp_df.drop_duplicates('title')['title'].values))
                item.extend(list(temp_df.drop_duplicates('title')['genres'].values))
                item.extend(list(temp_df.drop_duplicates('title')['tmdbId'].values))
    
    
                data.append(item)
    #index fetch
            # print(data)
            for i in data:
                index=data.index(i)
                tmdbid=data[index][2]
                images.append(fetch_poster(tmdbid))
            print(images)
        
        context={'data':data,'images':images}
        print(context)
    
    return render(request,'app/mylist.html',context)
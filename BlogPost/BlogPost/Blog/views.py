from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'coreyMS',
        'title':'blog post 1',
        'content':'first post content  .  .  .',
        'date_posted':'august 27 ,2018'
    }
    ,
    {
        'author':'jane doe',
        'title':'blog post 2',
        'content':'second post content  .  .  .',
        'date_posted':'august 28 ,2018'
    }
    ]


def home(request):
    context = { 
        'posts' : posts
    }
    return render(request,'Blog/home.html',context)

def about(request):
    return render(request,'Blog/about.html',{'title':'About'})


 
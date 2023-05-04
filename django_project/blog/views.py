from django.shortcuts import render
from .models import Menu
#from django.http import HttpResponse

posts = [
    {
        'author':'Mohamed Khaled',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27, 2023'
    },
    {
        'author':'Mohamed Zakaria',
        'title':'Blog Post 2',
        'content':'second post content',
        'date_posted':'August 28, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':"about"})

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu':newmenu}
    return render(request, 'blog/test.html', newmenu_dict)
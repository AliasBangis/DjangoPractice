from django.shortcuts import render

posts = [
    {
        'author': 'Ronald Langaoan',
        'title': 'ICpEP Project',
        'content': 'First Post Content',
        'date_posted': 'August 21, 2019'
    }
    
]

reserve = [
    {
        'author': 'Ronald Langaoan',
        'title': 'ICpEP Project',
        'content': 'First Post Content',
        'date_posted': 'August 21, 2019'
    }
    
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'proj/home.html', context)

def about(request):
    return render(request, 'proj/about.html', {'title': ' About'})
    

def reservation(request):
    context = {
        'reserve': reserve
    }
    return render(request,'proj/reservation.html',context)

def schedule(request):
    return render(request,'proj/schedule.html',{'title':' Schedule'})

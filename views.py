
from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'SUCCESS LAND',  
    }
    return render(request, 'success/index.html', context)

def about(request):
    return render(request, 'success/about.html')

def gallery(request):
    return render(request, 'success/gallery.html')

def videogallery(request):
    return render(request, 'success/videogallery.html')

def contact(request):
    return render(request, 'success/contact.html') 

def course1(request):
    return render(request, 'success/course1.html')

def course2(request):
    return render(request, 'success/course2.html')

def course3(request):
    return render(request, 'success/course3.html')
 
  


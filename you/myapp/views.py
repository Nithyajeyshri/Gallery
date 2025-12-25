from django.shortcuts import render

def gallery_view(request):
    return render(request, 'photo.html')
def home(request):
    return render(request, 'photo.html') 
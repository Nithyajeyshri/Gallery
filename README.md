# Ex.08 Design of Interactive Image Gallery
# Date:20-12-2025
# AIM:
To design a web application for an inteactive image gallery with minimum five images.

# DESIGN STEPS:
## Step 1:
Clone the github repository and create Django admin interface.

## Step 2:
Change settings.py file to allow request from all hosts.

## Step 3:
Use CSS for positioning and styling.

## Step 4:
Write JavaScript program for implementing interactivity.

## Step 5:
Validate the HTML and CSS code.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
views.py

from django.shortcuts import render

def gallery_view(request):
    return render(request, 'photo.html')
def home(request):
    return render(request, 'photo.html')

urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
]

photo.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Photo Gallery</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      margin: 0;
      padding: 20px;
    }
    h1 {
      text-align: center;
    }
    .gallery {
      display: grid;
      grid-template-columns: repeat(3, 1fr); 
      grid-template-rows: repeat(2, 200px);  
      gap: 15px;
      margin-top: 20px;
    }
    .gallery img {
      width: 70%;
      height: 100%;
      object-fit: cover;
      border-radius: 8px;
      transition: transform 0.5s ease;
    }
    .gallery img:hover {
      transform: scale(1.05);
    }

    
    .lightbox {
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(0,0,0,0.8);
      display: none;
      justify-content: center;
      align-items: center;
    }
    .lightbox img {
      max-width: 90%;
      max-height: 80%;
      border-radius: 10px;
    }
    .lightbox:target {
      display: flex;
    }
    .close {
      position: absolute;
      top: 20px;
      right: 30px;
      color: #fff;
      font-size: 30px;
      text-decoration: none;
    }
  </style>
</head>
<body>

<h1>My Photo Gallery</h1>
<div class="gallery">
  <a href="#img1"><img src="{% static 'images/R.jpg' %}" alt="Photo 1"></a>
  <a href="#img2"><img src="{% static 'images/img2.jpg' %}" alt="Photo 2"></a>
  <a href="#img3"><img src="{% static 'images/img3.jpg' %}" alt="Photo 3"></a>
  <a href="#img4"><img src="{% static 'images/img4.jpg' %}" alt="Photo 4"></a>
  <a href="#img5"><img src="{% static 'images/img5.jpg' %}" alt="Photo 5"></a>
  <a href="#img6"><img src="{% static 'images/img6.jpg' %}" alt="Photo 6"></a>
</div>

<div class="lightbox" id="img1">
  <a href="#" class="close">&times;</a>
  <img src="{% static 'images/R.jpg' %}" alt="Photo 1">
</div>
<div class="lightbox" id="img2">
  <a href="#" class="close">&times;</a>
  <img src="{% static 'images/img2.jpg' %}" alt="Photo 2">
</div>
<div class="lightbox" id="img3">
  <a href="#" class="close">&times;</a>
  <img src="{% static 'images/img3.jpg' %}" alt="Photo 3">
</div>
<div class="lightbox" id="img4">
  <a href="#" class="close">&times;</a>
  <img src="{% static 'images/img4.jpg' %}" alt="Photo 4">
</div>
<div class="lightbox" id="img5">
  <a href="#" class="close">&times;</a>
  <img src="{% static 'images/img5.jpg' %}" alt="Photo 5">
</div>
<div class="lightbox" id="img6">
  <a href="#" class="close">&times;</a>
  <img src="{% static 'images/img6.jpg' %}" alt="Photo 6">
</div>

</body>
</html>
```
# OUTPUT:
![alt text](<Screenshot (58).png>)
![alt text](<Screenshot (59).png>)
# RESULT:
The program for designing an interactive image gallery using HTML, CSS and JavaScript is executed successfully.

from django.shortcuts import render

# Home page
def index(request):
    boxes = ["MISSION", "VISION", "GOAL", "DESIRE", "PHILOSOPHY", "TESTAMENT"]
    return render(request, 'boxing_app/index.html', {'boxes': boxes})

# About page
def about(request):
    return render(request, 'boxing_app/about.html')

# Contact page
def contact(request):
    return render(request, 'boxing_app/contact.html')

# Mission page
def mission_view(request):
    return render(request, 'boxing_app/mission.html')

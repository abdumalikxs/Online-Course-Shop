from django.shortcuts import render
from django.http import HttpResponse  # importing HttpResponse class
# Create your views here.
# means in current file we want to find module called models.py
from .models import Course
# and import Course from there
# Without the dot, Python (not Django) searches from the project root where
# manage.py runs, so it skips your app folder.


def index(request):     # request that we get from user
    courses = Course.objects.all()
    # django will search courses.html inside the templates sub-directory that we created
    # we are passing courses sequence to render as 3rd argument
    # The key is just a label for a Python variable in the template,
    # meaning you can call it anything you want, but you must use that exact
    # label in the HTML file to access the data it refers to.
    return render(request, 'courses.html', {'courses': courses})

# A request is the HttpRequest object containing all details of the user’s HTTP call,
# triggered whenever the browser visits a URL
# The request in a view is always the HttpRequest object (not the button),
# carrying data sent by the browser.

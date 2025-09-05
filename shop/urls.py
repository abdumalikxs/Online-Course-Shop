from django.urls import path
from . import views   # '.' means current directory (package)

urlpatterns = [
    # expects from us a route and a view function (route, view)
    path('', views.index, name='index')
]
# '' - empty string means nothing more or root path.
# The name='index' part is giving a nickname (identifier) to that URL pattern.
# it allows us to later refer to this route in templates or code using its name.
# So  if someone visits root '' it executes index() function

from django.urls import path
from . import views   # '.' means current directory (package)

app_name = 'shop'
urlpatterns = [
    # expects from us a route and a view function (route, view)
    path('', views.index, name='index'),
    # since we will use this ID later we should do it like this '<int:course_id>'
    path('<int:course_id>', views.single_course, name='single_course')
]
# '' - empty string means nothing more or root path.
# The name='index' part is giving a nickname (identifier) to that URL pattern.
# it allows us to later refer to this route in templates or code using its name.
# So  if someone visits root '' it executes index() function
# <int:course_id> captures an integer from the URL
#  and passes it as the variable course_id to the view function.

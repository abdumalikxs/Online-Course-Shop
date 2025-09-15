from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

# api/v1/courses/         GET, POST
# api/v1/courses/1/       GET, DELETE
# api/v1/categories/      GET
# api/v1/categories/1/    GET

api = Api(api_name='v1')
# We create instances so Tastypie can register and expose them as working API endpoints.
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

# Now after registration the routes to our resources will be like this:
# api/v1/courses
# api/v1/categories

urlpatterns = [
    path('', include(api.urls), name='index')
]

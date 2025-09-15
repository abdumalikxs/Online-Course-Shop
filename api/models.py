from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization   # Authorization is a class.
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta():
        queryset = Category.objects.all()
        # It tells Tastypie what the endpoint URL for this resource should look like.
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta():
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        # we create instance of CustomAuthentication so API can use our is_authenticated via instance
        authentication = CustomAuthentication()
        # If you wanted more control (e.g., only the course owner can delete), you’d replace this with a custom Authorization class.
        authorization = Authorization()
        excludes = ['reviews_qty', 'created_at']

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']  # return's 1
        return bundle

    def dehydrate(self, bundle):
        # returns __str__'s result
        # if we do category_id it will return nubmer of cateogry instead of str
        bundle.data['category_id'] = bundle.obj.category_id
        # create new object withing json with key "category"
        bundle.data['category'] = bundle.obj.category
        return bundle

    # •	Hydrate = JSON input → model
    # • Dehydrate = model → JSON output

        # •	hydrate → runs on POST/PUT (input JSON → model instance).
        # •	dehydrate → runs on GET (model instance → JSON output).

    def dehydrate_title(self, bundle):
        # converts JSON's title into upper.
        return bundle.data['title'].upper()

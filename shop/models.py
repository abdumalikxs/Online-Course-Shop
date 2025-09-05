from django.db import models
from django.utils import timezone

# Create your models here.
# parent class


class Category(models.Model):   # Model for a Category
    # now we indicate what fields will be there in database
    #  we do it using attributes of a class
    # Charfield means value will be in 'str' type
    title = models.CharField(max_length=255)
    # date will be generated automatically
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  # returns the name of the title


class Course(models.Model):  # Model for a Course
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    # Foreign key means key from a different table
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
# on_delete=models.CASCADE  --> means that when deleting specific category,
# automatically the Course instances of it will be deleted as well.
    # date will be generated automatically
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Note that all this was made not writing even a line of SQL request

from django.db import models
from django.contrib.auth.models import User

class Book (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    title= models.CharField(max_length=155)
    author= models.CharField(max_length=155)
    isbn_number = models.CharField(max_length=13, null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)
    categories= models.ManyToManyField("Category", through='BookCategory', related_name='books')
#It is important to note that categories is not an actual field in the database. It is a property that exist on instances of Book that will automatically contain all of the related categories for the book.
#The first argument is the name of the table that is the other side of the many-to-many relationship - Category.
#The second argument tells Django which model will store those relationships - BookCategory.
#The third argument is what property will be added to instances of the Category model to contain a list of related books - books.
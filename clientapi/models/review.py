from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Review (models.Model):
    book=models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment=models.TextField(max_length=155)
    created_on=models.DateField(auto_now_add=True)
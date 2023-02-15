from django.db import models
from django.contrib.auth.models import User
import django.core.validators
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class CarReview(models.Model):
    formula_name = models.CharField(max_length=200, unique=True)        # formula 1 and IndyCar
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author")
    # updated_on = models.DateTimeField()
    rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    review = models.TextField()
    feature_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

class CarComment(models.Model):
    car_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"


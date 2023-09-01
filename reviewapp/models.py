from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class CarReviewModel(models.Model):
    """
    Main car review page by author
    """
    formula_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_author")
    updated_on = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    review_by_admin = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
                                   User, related_name='review_likes',
                                   blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.formula_name + ' | ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('review_detail')


class CarCommentModel(models.Model):
    """
    Comments from Users
    """
    comment_user = models.ForeignKey(CarReviewModel, on_delete=models.CASCADE,
                                     related_name='comments_by_user')
    username = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_by_admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.username}"

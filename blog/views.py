from django.shortcuts import render
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    template_name = "index.html"
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6         # limit the nr of review

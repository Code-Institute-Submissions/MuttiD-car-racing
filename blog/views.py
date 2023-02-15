from django.shortcuts import render
from django.views import generic
from .models import CarReview


class ReviewList(generic.ListView):
    model = CarReview
    queryset = CarReview.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6         # limit the nr of reviews

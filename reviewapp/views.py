from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import CarReview, CarComment
from django.http import HttpResponseRedirect


class ReviewList(ListView):
    model = CarReview
    queryset = CarReview.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6         # limit the nr of reviews
    context_object_name = 'reviews'


class ReviewDetail(ListView):

    def get(self, request, slug, *args, **kwargs):
        queryset = CarReview.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = CarReview.objects.filter(
            approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "review_details.html",
            {
                "review": review,
                # "comments": car_comment,
                "liked": liked,
            },
        )

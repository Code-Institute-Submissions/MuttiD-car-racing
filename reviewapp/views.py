from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import DetailView, ListView
from .models import CarReview, CarComment
from django.http import HttpResponseRedirect
from .forms import CommentForm


class ReviewList(ListView):
    """
    A List of the Cars' Reviews
    """
    model = CarReview
    queryset = CarReview.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 4         # limit the nr of reviews
    # context_object_name = 'reviews'


class ReviewDetail(ListView):
    """
    Returns full detail of the review
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = CarReview.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by(
                                            'created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "review_details.html",
            {
                "review": review,
                # "comments": car_comment,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Returns details with approved reviews
        Logged in users can submit a comment for approval
        """
        queryset = CarReview.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = CarReview.objects.filter(
            approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "review_details.html",
            {
                "review": review,
                # "comments": car_comment,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class ReviewLike(ListView):
    """
    Review likes counted. Total likes displayed
    """
    def review(self, request, slug):
        review = get_object_or_404(Post, slug=slug)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))

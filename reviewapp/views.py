from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CarReviewModel, CarCommentModel
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.urls import reverse


class ReviewDetailList(ListView):
    """
    A List of the Cars' Reviews
    """
    model = CarReviewModel
    queryset = CarReviewModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4         # limit the nr of reviews
    # context_object_name = 'reviews'


class ReviewDetailView(DetailView):
    """
    Returns full detail of the review
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = CarReviewModel.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comment_user.filter(approved=True).order_by(
                                            'created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "CommentForm": CommentForm,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Returns details with approved reviews
        Logged in users can submit a comment for approval
        """
        queryset = CarReviewModel.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.objects.filter(
            approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_details.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form,
            },
        )


class ReviewCommentView(View):
    """
    Once the user is logged in, it will allow
    the user to create a comment
    """
    template_name = "review_comments.html"
    form_class = CommentForm


class ReviewLike(View):
    """
    Review likes counted. Total likes displayed
    """
    def post(self, request, slug):
        review = get_object_or_404(CarReviewModel, slug=slug)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail',
                                    args=[review.slug]))

from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, DetailView, ListView
from django.contrib import messages
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


def review_detail(request, slug, *args, **kwargs):
    """
    This function-based view will allow users to view
    the detail of a review.    
    """

    queryset = CarReviewModel.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments_by_user.all().order_by("-created_on")
    comment_count = post.comments_by_user.filter(approved_by_admin=True).count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.comment_user = post
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment awaiting moderation.')
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "review_details.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )


def update_comment(request, review_id, *args, **kwargs):
    """
    This view will allow users to update their comments 
    """
    if request.method == "POST":

        queryset = CarReviewModel.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        new_comment = post.new_comment.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=new_comment)
        if comment_form.is_valid() and new_comment.name == request.user.username:
            update_comment = comment_form.save(commit=False)
            update_comment.post = post
            update_comment.approved_by_admin = False
            update_comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def comment_delete(request, slug, comment_id, *args, **kwargs):
    """
    A view to delete user's comment
    """
    queryset = CarCommentModel.objects.filter(status=1)
    post = get_object_or_404(queryset)
    new_comment = post.comments.filter(id=comment_id).first()

    if new_comment.name == request.user.username:
        new_comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def review_like(request, slug, *args, **kwargs):
    """
    Review likes counted. Total likes will be displayed
    """
    post = get_object_or_404(CarReviewModel, slug=slug)
    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('review_details', args=[slug]))

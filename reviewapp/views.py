from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, DetailView, ListView, FormView
from django.contrib import messages
from reviewapp.models import CarReviewModel, CarCommentModel, Contact
from django.http import HttpResponseRedirect
from reviewapp.forms import CommentForm, ContactForm
from django.urls import reverse


class ReviewDetailList(ListView):
    """
    A List of the Cars' Reviews
    """
    model = CarReviewModel
    queryset = CarReviewModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4         # limit the nr of reviews


def review_detail(request, slug, *args, **kwargs):
    """
    This function-based view will allow users to view
    the detail of a review.
    """

    queryset = CarReviewModel.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments_by_user.filter(approved_by_admin=True).order_by("-created_on")
    comment_count = post.comments_by_user.filter(approved_by_admin=True).count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.username = request.user.username
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


def update_comment(request, comment_id):
    """
    This view will allow users to update their comments
    """

    update_c = CarCommentModel.objects.get(pk=comment_id)
    update_form = CommentForm(request.POST or None, instance=update_c)

    if update_c.comment_user.author != request.user:
        return redirect("all_reviews")

    if update_form.is_valid():  # Fixed the form variable name
        update_form.save()
        return redirect("all_reviews")
    return render(request, "update_comment.html", {'update_form': update_form})


def delete_comment(request, comment_id):
    """
    A view to delete a user's comment
    """
    delete_c = CarCommentModel.objects.get(pk=comment_id)
    context = {'delete_c': delete_c}

    if request.method == 'POST':
        if delete_c.comment_user.author != request.user:  # Fixed the condition
            return redirect("all_reviews")

        delete_c.delete()
        messages.success(request,
                         ("You have deleted this comment"))
        return redirect("all_reviews")

    return render(request, "delete_comment.html", context)


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/success'

    def form_valid(self, form):
        form.save()    
        messages.success(self.request, 'Thank you for your message. We will get back to you soon!')    
        return super().form_valid(form)

    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message. We will get back to you soon!')
            return redirect('success')
        return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')


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

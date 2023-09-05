from . import views
from django.urls import path
# from .views import ReviewDetailView

urlpatterns = [
    path('', views.ReviewDetailList.as_view(), name='all_reviews'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete,
         name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.update_comment,
         name='update_comment'),
    path('like/<slug:slug>', views.review_like, name='review_like')
]

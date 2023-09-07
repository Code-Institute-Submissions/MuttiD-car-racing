from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewDetailList.as_view(), name="all_reviews"),
    path('review_detail/<slug:slug>/',
         views.review_detail, name="review_detail"),
    path('like/<slug:slug>', views.review_like, name="review_like"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('success/', views.success, name="success"),
    path('update_comment/<int:comment_id>/', 
         views.update_comment, name="update_comment"),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment, name="delete_comment")
]

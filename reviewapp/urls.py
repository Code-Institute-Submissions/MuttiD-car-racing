from . import views
from django.urls import path
from .views import ReviewDetailView

urlpatterns = [
    path('', views.ReviewDetailList.as_view(), name='all_reviews'),
    path('review_comments', views.ReviewCommentView.as_view(),
         name='review_comments'),
    path('like/<slug:slug>/', views.ReviewLike.as_view(), name='review_like'),
    path('<slug:slug>/', views.ReviewLike.as_view(),
         name='review_detail'),
]

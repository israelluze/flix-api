from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.ReviewListCreateView.as_view(), name='review_create_list'),
    path('review/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review_update_detail')
]

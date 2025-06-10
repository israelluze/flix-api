from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreListCreateView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>/', views.GenreRetriveUpdateDestroyView.as_view(), name='genre_update_detail'),
]

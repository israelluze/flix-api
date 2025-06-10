from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalPermissions
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissions]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissions]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

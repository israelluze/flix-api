from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalPermissions
from actors.models import Actor
from actors.serializers import ActorSerializer

class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissions]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissions]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer   

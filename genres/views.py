from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer    

# @csrf_exempt
# def genre_create_list_view():
    
#     if request.method == 'GET':    
#         genres = Genre.objects.all().values('id', 'name')
#         return JsonResponse(list(genres), safe=False)
#     elif request.method == 'POST':        
#         data = json.loads(request.body.decode('utf-8'))
#         if data:
#             name = data['name']
#             genre = Genre(name=name)
#             genre.save()
#             return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)
#         return JsonResponse({'error': 'Name is required'}, status=400)
    
#     return JsonResponse({'error': 'Invalid request method'}, status=405)



# @csrf_exempt
# def genre_update_detail_view(request, pk): 
       
    
#     genre = get_object_or_404(Genre, pk=pk)    

#     if request.method == 'GET':
#         return JsonResponse({'id': genre.id, 'name': genre.name})
    
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         if 'name' in data:
#             genre.name = data['name']
#             genre.save()
#             return JsonResponse({'id': genre.id, 'name': genre.name})
#         return JsonResponse({'error': 'Name is required'}, status=400)
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': 'Genre deleted successfully'}, status=204)
    
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


        

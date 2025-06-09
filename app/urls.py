from django.contrib import admin
from django.urls import path, include
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),   
    
    path('api/v1/', include('authenticate.urls')) ,
    
    path('api/v1/', include('genres.urls')),
    
    path('api/v1/', include('actors.urls')),
    
    path('api/v1/', include('movies.urls')),  
    
    path('api/v1/', include('reviews.urls')),  
    

]

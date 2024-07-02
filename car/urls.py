
from django.urls import path 
from django.conf.urls.static import static
from . import views
urlpatterns = [
    
    path('car-details/<int:id>/', views.DetailsCarView.as_view(), name='car_details'),
    
    
]
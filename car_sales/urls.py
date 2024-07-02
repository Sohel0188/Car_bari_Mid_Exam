"""
URL configuration for car_sales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('login', views.user_login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),

    path('register', views.user_register, name='register'),
    # path('logout', views.user_logout, name='logout'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'), 
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('category/<slug:brand_slug>/', views.home, name='brand_wise_car'),
    path('buycar/<int:id>/', views.buyCar, name='buy_car'),
    path('car/', include('car.urls')),
    # path('car-details/<int:id>/', views.DetailsCarView, name='car_details'),
    
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

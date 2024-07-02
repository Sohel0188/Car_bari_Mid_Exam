from django.shortcuts import render, redirect,get_object_or_404
from . import forms
# from .forms import RegistrationForm
from car.models import Car, Comment, BuyCar
from brand.models import Brand
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View

def home(request, brand_slug = None):
    title = 'Home'
    cars = Car.objects.all()
    total_cars = cars.count()
    brands = Brand.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug= brand_slug)
        cars = Car.objects.filter(brand = brand)
        total_cars = cars.count()
    return render (request, 'home.html', {'title': title, 'cars': cars, 'brands': brands, 'total_cars': total_cars})


def user_register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
            return redirect('profile')
    else:
        form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : form})


# def user_login(request):
#     if request.method=="POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username= user_name, password= user_pass)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Logged in successfully')
#                 return redirect('profile')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form':form} )


class UserLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def profile(request):
        purchased_cars = BuyCar.objects.filter(user=request.user).select_related('car')
        return render(request, 'profile.html', {'purchased_cars':purchased_cars})


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance= request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            
            form = forms.ChangeUserData(instance= request.user)
        return render(request, 'edit_profile.html', {'form' : form})
    else:
        return redirect('login')
  

@login_required
def buyCar(request, id):
    car = get_object_or_404(Car, pk=id)
    if not BuyCar.objects.filter(car=car, user=request.user).exists():
        BuyCar.objects.create(car=car, user=request.user)
        car.qunatity -= 1 
        car.save()
   
    return redirect('profile')
            

# def user_logout(request):
#     logout(request)
#     messages.success(request, ' Successfully Logged Out ')
#     return redirect('home')

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Successfully Logged Out')
        return redirect(reverse_lazy('home'))

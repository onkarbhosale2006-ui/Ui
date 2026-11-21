from django.urls import path
from . import views

urlpatterns = [

    # Public
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    # After Login
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transactions/', views.transactions, name='transactions'),
    path('budgets/', views.budgets, name='budgets'),
    path('goals/', views.goals, name='goals'),
    path('profile/', views.profile, name='profile'),
]
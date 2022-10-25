from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('methodology/', views.methodology),
    path('about_us/', views.about_us),
    path('models_MV/', views.models_MV),
    path('models_CVaR/', views.models_CVaR),
    path('models_Omega/', views.models_Omega),



    # needs to remove after done the initiate
    path('init_db/', views.init_db),
]
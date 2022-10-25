from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('methodology/', views.methodology),
    path('about_us/', views.about_us),
    path('models/', views.models),


    #test route
    path('test/', views.get_period_date),
    # needs to remove after done the initiate
    path('init_db/', views.init_db),
]
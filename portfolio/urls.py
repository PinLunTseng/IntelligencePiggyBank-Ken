from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'portfolio'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('methodology/', views.methodology),
    path('about_us/', views.about_us),
    path('models_MV/', views.models_MV),
    path('models_CVaR/', views.models_CVaR),
    path('models_Omega/', views.models_Omega),
    path('login/', views.user_login, name='login'),
    path('create_user/', views.create_user),
    path('portfolio_list/', views.portfolio_list),

    path('risk_preference_measurement/', views.risk_preference_measurement),
    path('form_test/', views.form_test),
    # needs to remove after done the initiate
    path('init_db/', views.init_db),
]
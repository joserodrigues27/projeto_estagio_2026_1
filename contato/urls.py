from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='landpage'), name='logout'),
    path('painel/', views.painel_mensagens, name='painel')
]

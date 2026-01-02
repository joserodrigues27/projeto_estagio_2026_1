from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='landpage'), name='logout'),
    path('painel/', views.painel_mensagens, name='painel'),
    path('painel/pesquisa/', views.painel_pesquisa, name='painel_pesquisa'),
    path('painel/mensagem/<int:mensagem_id>/', views.detalhe_mensagem, name='detalhe_mensagem'),
    path('painel/mensagem/<int:mensagem_id>/apagar/', views.apagar_mensagem, name='apagar_mensagem'),
    path('painel/mensagem/<int:mensagem_id>/confirmar/', views.confirmar_exclusao, name='confirmar_exclusao')
]

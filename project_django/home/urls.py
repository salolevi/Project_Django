from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="main_index"),
    path('create-ticket', views.CreateTicketView.as_view(), name="createticket-form"),
    path('create-ticket/nuevo', views.CreateTicketView.as_view(), name="create-ticket"),
    path('usuarios', views.UsuariosView.as_view(), name='usuarios'),
    path('crear-usuario', views.CrearUsuario.as_view(), name='createuser-form'),
    path('crear-usuario/nuevo', views.CrearUsuario.as_view(), name="createuser"),
    path('analistas', views.AnalistasView.as_view(), name='analistas'),
    path('crear-analista', views.CrearAnalista.as_view(), name='createanalist-form'),
    path('crear-analista/nuevo', views.CrearAnalista.as_view(), name="createanalist")
]

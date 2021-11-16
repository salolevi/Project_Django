from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="main_index"),
    path('signup-form', views.SignUpForm.as_view(), name='signup'),
    path('signup-form/create', views.SignUpForm.as_view(), name='signup-create'),
    path('login-form', views.LogInForm.as_view(), name="login"),
    path('admin-page', views.AdminView.as_view(), name='admin'),
    path('admin-page/logout', views.AdminView.as_view(), name='admin-logout'),
    path('create-ticket', views.CreateTicketView.as_view(), name="createticket-form"),
    path('create-ticket/nuevo', views.CreateTicketView.as_view(), name="create-ticket"),
    path('usuarios', views.UsuariosView.as_view(), name='usuarios'),
    path('crear-usuario', views.CrearUsuario.as_view(), name='createuser-form'),
    path('crear-usuario/nuevo', views.CrearUsuario.as_view(), name="createuser"),
    path('analistas', views.AnalistasView.as_view(), name='analistas'),
    path('crear-analista', views.CrearAnalista.as_view(), name='createanalist-form'),
    path('crear-analista/nuevo', views.CrearAnalista.as_view(), name="createanalist"),
    path('plantas', views.PlantasView.as_view(), name='plantas'),
    path('crear-planta', views.CrearPlanta.as_view(), name='createplant-form'),
    path('crear-planta/nuevo', views.CrearPlanta.as_view(), name='createplant')
]

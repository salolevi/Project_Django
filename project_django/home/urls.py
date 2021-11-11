from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="main_index"),
    path('create-ticket', views.CreateTicketView.as_view(), name="create-ticket")

]

from django.urls import path
from BibliotecaApp import views
from django.contrib.auth.views import LogoutView
from django import views
from django.urls import path
from .views import LoginPagina, RegistroPagina, inicio, UsuarioEdicion, CambioPassword
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    
    path('', inicio.as_view(), name='inicio'),
    path('musica/', views.musica, name="Musica"),
    path('libros/', views.libros, name="Libros"),
    path('peliculas/', views.peliculas, name="Peliculas"),
    path('libros/libroFormulario/', views.libroFormulario, name="Formulario Libro"),
    path('guardar_libro/', views.guardar_libro, name="Guardar Libro"),
    path('libroBusqueda/', views.libroBusqueda, name="Busqueda Libro"),
    path('resultados/', views.resultados, name="Resultados"),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='edicionPerfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),

    path('acercaDeMi/', views.about, name='acerca de mi'),



]

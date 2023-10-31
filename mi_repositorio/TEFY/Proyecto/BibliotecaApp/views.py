from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaApp.models import Libro, Pelicula, Musica
from BibliotecaApp.forms import LibroFormulario, FormularioCambioPassword
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import FormularioRegistroUsuario, FormularioEdicion, LibroFormulario
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# Create your views here.

class inicio(LoginRequiredMixin, TemplateView):
    template_name = 'BibliotecaApp/base.html'


class LoginPagina(LoginView):
    template_name = 'BibliotecaApp/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')
    
class RegistroPagina(FormView):
    template_name = 'BibliotecaApp/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(RegistroPagina, self).get(*args, **kwargs)


def musica(request):
    return render(request, "BibliotecaApp/musica.html")

def libros(request):
    return render(request, "BibliotecaApp/libros.html")

def peliculas(request):
    return render(request, "BibliotecaApp/peliculas.html")

def libroFormulario(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        genero = request.POST.get('genero')

        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero)
        nuevo_libro.save()

        return render(request, "BibliotecaApp/inicio.html")

    return render(request, "BibliotecaApp/libroFormulario.html")

def libroBusqueda (request):
    return render(request, "BibliotecaApp/libroBusqueda.html")

def resultados(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, "BibliotecaApp/resultados.html", {'libros': libros, 'titulo': titulo})

    else:
        respuesta = "No enviaste datos."


    return HttpResponse(respuesta)


class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'BibliotecaApp/edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user
    
class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'BibliotecaApp/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'BibliotecaApp/passwordExitoso.html', {})

class LibroCreacion(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroFormulario
    success_url = reverse_lazy('inicio')
    template_name = 'BibliotecaApp/libroFormulario.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LibroCreacion, self).form_valid(form)
    
def guardar_libro(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        genero = request.POST.get('genero')

        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero)
        nuevo_libro.save()

        return render(request, "BibliotecaApp/libros.html")

    return HttpResponse("Error al guardar el libro")

def lista_libros(request):
    libros = Libro.objects.all()  # Obtener todos los libros
    return render(request, 'BibliotecaApp/libros.html', {'libros': libros})

def about(request):
    return render(request, 'BibliotecaApp/acercaDeMi.html', {})
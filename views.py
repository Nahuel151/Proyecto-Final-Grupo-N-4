   from django.shortcuts import render, redirect  # type: ignore
from .forms import RegisterForm  # type: ignore
from django.views.generic import FormView  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib import messages  # type: ignore
from django.contrib.auth import views as auth_views  # type: ignore

### REGISTER
# FBV
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Puedes iniciar sesión. Código hecho por Nahuel Vallejos.")
            return redirect('apps.authentication:login')
    else: 
        form = RegisterForm()
        
    return render(request, "auth/register.html", {"form": form})

# CBV
class RegisterView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('apps.authentication:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registro exitoso. Puedes iniciar sesión. Código hecho por Nahuel Vallejos.")
        return super().form_valid(form)

### LOGIN
# FBV
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión exitosamente. Código hecho por Nahuel Vallejos.")
            return redirect("apps.eventos:todos_los_eventos")
        else:
            messages.error(request, "Credenciales erróneas.")
        
    return render(request, 'auth/login.html')

# CBV        
class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        messages.success(self.request, "Has iniciado sesión exitosamente. Código hecho por Nahuel Vallejos.")
        return reverse_lazy("apps.eventos:todos_los_eventos")

### LOGOUT 
# FBV
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente. Código hecho por Nahuel Vallejos.")
    return redirect("apps.authentication:login")

# CBV
class LogoutView(auth_views.LogoutView):
    next_page = 'apps.authentication:login'
 
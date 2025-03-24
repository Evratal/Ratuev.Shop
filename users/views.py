import secrets

from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
from django.core.mail import send_mail

class UserCreateView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"

        send_mail (
            subject = 'Подтверждение почты',
            message = f'Добрый день, перейдите по ссылке для подтверждения почты {url}!',
            from_email = EMAIL_HOST_USER,
            recipient_list = [user.email],)
        return super().form_valid(form)




def email_verification(request,token):
        user = get_object_or_404(User, token=token)
        user.is_active = True
        user.save()
        return redirect(reverse("users:login"))


@require_http_methods(["POST"])  # Разрешаем только POST-запросы
def simple_logout(request):
    """Безопасный выход из системы"""
    logout(request)
    return redirect('catalog:product_list')
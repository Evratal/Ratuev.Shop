import secrets
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

from config.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
from django.core.mail import send_mail

class UserCreateView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        user = form.save
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http//{host}/users/email_confirm/{token}/"

        send_mail (
            subject = 'Добро пожаловать в наш сервис',
            message = 'Спасибо, что зарегистрировались в нашем сервисе!',
            from_email = EMAIL_HOST_USER,
            recipient_list = [user.email],)
        return super().form_valid(form)




def email_verification(request,token):
        user = get_object_or_404(token=token)
        user.is_active = True
        user.save()
        return redirect(reverse("users:login"))

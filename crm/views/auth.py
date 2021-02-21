from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import authenticate, login, logout


class LoginView(TemplateView):
    template_name = 'auth/index'

    def get(self, request, *args, **kwargs):
        return super().get(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request=request, *args, **kwargs)


class LogoutView(RedirectView):
    pattern_name = 'auth/index'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
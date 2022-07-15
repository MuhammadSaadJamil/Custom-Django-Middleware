from django.shortcuts import redirect
from django.urls import reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated or str(request.path) == reverse('login'):
            return self.get_response(request)
        return redirect(reverse('login'))

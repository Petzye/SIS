from django.shortcuts import render
from django.views import View
from .models import User

# Create your views here.


class LoginView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        users = User.objects.create_user(
            username='', firstname='', lastname='', password='')  # Select * from users
        xx = user.firstname

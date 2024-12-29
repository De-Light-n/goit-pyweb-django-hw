from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="users/login.html", form_class=LoginForm), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', views.logoutuser, name='logout'),
]

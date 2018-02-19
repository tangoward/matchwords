
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]

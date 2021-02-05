from django.urls import path

from .views import (
    RegisterUserView
)


app_name = 'auth'
urlpatterns = [
    #ex: /accounts/register
    path('register/', RegisterUserView.as_view(), name='register'),

    #ex: /accounts/login
]

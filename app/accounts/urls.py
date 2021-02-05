from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterUserView
)


app_name = 'auth'
urlpatterns = [
    # ex: /accounts/create/
    path('create/', RegisterUserView.as_view(), name='create_user'),

    # ex: /accounts/token/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # ex: /accounts/token/refresh/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

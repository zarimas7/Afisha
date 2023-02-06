from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('registration/', views.RegistrationAPiView.as_view()),
]
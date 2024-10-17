from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.CreatePerson),
    path('user/', views.CreateUserView.as_view()),
]

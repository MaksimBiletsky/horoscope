from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.UserProfileList.as_view()),
]

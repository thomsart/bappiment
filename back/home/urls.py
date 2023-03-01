from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

home_urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
]

home_urlpatterns = format_suffix_patterns(home_urlpatterns)
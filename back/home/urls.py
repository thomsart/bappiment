from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

home_urlpatterns = [
    path('status/', views.StatusList.as_view(), name='status-list'),
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('memberships/', views.MembershipList.as_view(), name='memberships-list'),
    path('memberships/<int:pk>/', views.MembershipDetail.as_view(), name='membership-detail'),
]

home_urlpatterns = format_suffix_patterns(home_urlpatterns)

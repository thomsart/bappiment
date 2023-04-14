from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import status_views, users_views, memberships_views


home_urlpatterns = [
    path('status/', status_views.StatusViews.as_view({'get':'list'}), name='status-list'),
    path('status/<int:pk>/', status_views.StatusViews.as_view({'get':'retrieve'}), name='status-detail'),
    path('users/', users_views.CustomUserList.as_view(), name='users-list'),
    path('users/<int:pk>/', users_views.CustomUserDetail.as_view(), name='users-detail'),
    path('memberships/', memberships_views.MembershipList.as_view(), name='memberships-list'),
    path('memberships/<int:pk>/', memberships_views.MembershipDetail.as_view(), name='memberships-detail'),
]

home_urlpatterns = format_suffix_patterns(home_urlpatterns)
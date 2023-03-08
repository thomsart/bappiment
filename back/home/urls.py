from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import memberships_views, status_views, users_views


home_urlpatterns = [
    path('status/', status_views.StatusList.as_view(), name='status-list'),
    path('users/', users_views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', users_views.UserDetail.as_view(), name='user-detail'),
    path('memberships/', memberships_views.MembershipList.as_view(), name='memberships-list'),
    path('memberships/<int:pk>/', memberships_views.MembershipDetail.as_view(), name='membership-detail'),
]

home_urlpatterns = format_suffix_patterns(home_urlpatterns)

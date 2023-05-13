from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import entities_views, clients_views, installations_views


client_urlpatterns = [
    path('entities/', entities_views.LegalEntityViews.as_view({'get':'list'}), name='entities-list'),
    path('entities/<int:pk>/', entities_views.LegalEntityViews.as_view({'get':'retrieve'}), name='entities-detail'),
    path('clients/', clients_views.ClientList.as_view(), name='clients-list'),
    path('clients/<int:pk>/', clients_views.ClientDetail.as_view(), name='clients-detail'),
    path('installations/', installations_views.InstallationList.as_view(), name='installations-list'),
    path('installations/<int:pk>/', installations_views.InstallationDetail.as_view(), name='installations-detail'),
]

client_urlpatterns = format_suffix_patterns(client_urlpatterns)
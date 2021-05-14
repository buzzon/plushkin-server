from django.conf.urls import url

from rest_framework.authtoken import views as rest_views
from . import views
from .views import UserViewSet, BookmarkViewSet, BookmarkLinkViewSet

app_name = 'core'
urlpatterns = [
    url(r'user_registration/$', views.UserCreate.as_view(), name="user_registration"),
    url(r'user/$', views.get_user, name="user"),
    url(r'user_update/$', views.user_update, name="user_update"),
    url(r'user_remove/$', views.user_remove, name="user_remove"),
    url(r'auth_token/$', rest_views.obtain_auth_token, name="get_token"),
    url(r'users/$', UserViewSet.as_view({'get': 'list'}), name='genres_list'),
    url(r'bookmarks/$', BookmarkViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-list'),
    url(r'bookmarks/(?P<pk>[^/]+)$', BookmarkViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'}), name='account-retrieve'),
    url(r'bookmarks/link/(?P<pk>[^/]+)$', BookmarkLinkViewSet.as_view({'get': 'retrieve', 'post': 'update'}), name='account-retrieve'),
]

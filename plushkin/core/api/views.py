from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets

from core.api.serializers import UserSerializer, BookmarkSerializer, BookmarkLinkSerializer
from core.models import Bookmark


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('type', )

    def get_queryset(self):
        return self.request.user.bookmarks.all()


class BookmarkLinkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkLinkSerializer
    queryset = Bookmark.objects.all()


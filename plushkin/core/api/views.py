from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.api.filters import BookmarkFilter
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
    filterset_class = BookmarkFilter

    def get_queryset(self):
        return self.request.user.bookmarks.all()


class BookmarkLinkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkLinkSerializer
    queryset = Bookmark.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    content = {
        'username': str(request.user.username),
        'first_name': str(request.user.first_name),
        'email': str(request.user.email),
    }
    return Response(content)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_update(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.data['first_name']
        user.email = request.data['email']
        user.username = request.data['email']
        user.save()
    return Response({'ok': 'ok'})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_remove(request):
    if request.method == 'POST':
        user = request.user
        user.delete()

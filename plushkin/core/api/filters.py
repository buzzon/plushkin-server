from django_filters import rest_framework as filters

from core.api.serializers import BookmarkSerializer
from core.models import Bookmark


# class BookmarkFilter(filters.FilterSet):
#     queryset = Bookmark.objects.all()
#     serializer_class = BookmarkSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_fields = ('type', 'date')
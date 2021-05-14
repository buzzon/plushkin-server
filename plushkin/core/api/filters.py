import django_filters
from django.db import models
from django.db.models import Q

from core.models import Bookmark


class BookmarkFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='my_custom_filter')

    def my_custom_filter(self, queryset, name, value):
        return Bookmark.objects.filter(
            Q(title__icontains=value) | Q(siteName__icontains=value)
        )

    class Meta:
        model = Bookmark
        fields = {
            'type': ['exact'],
        }


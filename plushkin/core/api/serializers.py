from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from core.models import Bookmark


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}, 'date': {'read_only': True}, 'type': {'required': False}}

    def create(self, validated_data):
        bookmark = Bookmark(
            title=validated_data['title'],
            url=validated_data['url'],
            type=self.data.get('type', Bookmark._meta.get_field('type').get_default()),
            user=self.context['request'].user,
        )
        bookmark.save()
        return bookmark


class BookmarkLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['url']
        extra_kwargs = {'url': {'read_only': True}}
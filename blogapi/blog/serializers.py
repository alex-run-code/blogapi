from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']

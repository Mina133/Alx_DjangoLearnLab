from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields =['author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['author', 'content', 'created_at', 'comments']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

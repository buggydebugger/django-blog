from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework.fields import CurrentUserDefault


from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    slug = serializers.CharField(max_length=100, read_only=True)
    author = UserSerializer(read_only=True)

    def create(self, validated_data):
        validated_data.update({'author': self.context['request'].user,
                               'slug': slugify(validated_data.get('title'))})
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = self.context['request'].user
        instance.slug = slugify(validated_data.get('title'))
        instance.save()
        return instance




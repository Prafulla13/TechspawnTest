from rest_framework import serializers
from .models import blogs


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogs
        fields = (
            'blog_name',
            'blog_body',
            'blog_technology',
            'user',
            'status',
            'created_by',
            'created_on',
            'updated_by',
            'updated_on')

    def update(self, instance, validated_data):
        instance.blog_name = validated_data.get(
            "blog_name", instance.blog_name)
        instance.blog_body = validated_data.get(
            "blog_body", instance.blog_body)
        instance.blog_technology = validated_data.get(
            "blog_technology", instance.blog_technology)
        instance.user = validated_data.get(
            "user", instance.user)
        instance.status = validated_data.get(
            "status", instance.status)
        instance.created_by = validated_data.get(
            "created_by", instance.created_by)
        instance.updated_by = validated_data.get(
            "updated_by", instance.updated_by)
        instance.updated_on = validated_data.get(
            "updated_on", instance.updated_on)
        instance.save()
        return instance

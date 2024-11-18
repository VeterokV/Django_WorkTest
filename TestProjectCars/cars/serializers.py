from rest_framework import serializers
from .models import Car, Comment


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'carmodel', 'year', 'desc', 'created_at', 'updated_at', 'id_owner']
        read_only_fields = ['id_owner']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'id_car', 'id_auth']
        read_only_fields = ['id_auth']

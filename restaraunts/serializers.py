from rest_framework import serializers
from .models import Restaurant, Menu, Vote
from .models import Vote



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'location']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'items']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['choice', 'voted_at']



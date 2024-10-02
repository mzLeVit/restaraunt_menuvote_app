from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer
from datetime import date
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.db import models
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta





class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(date=date.today())

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'choice')  # Користувач може голосувати тільки один раз

class CheckVoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if Vote.objects.filter(user=user).exists():
            return Response({'voted': True}, status=status.HTTP_200_OK)
        return Response({'voted': False}, status=status.HTTP_200_OK)


class VoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        choice = request.data.get('choice')
        today = datetime.now()

        # Перевірка, чи голосував користувач сьогодні
        try:
            vote = Vote.objects.get(user=user)
            time_since_vote = today - vote.voted_at

            if time_since_vote < timedelta(days=1):
                return Response({'detail': 'You can only vote once per day'}, status=status.HTTP_400_BAD_REQUEST)

            # Якщо голосування дозволене, оновлюємо вибір
            vote.choice = choice
            vote.voted_at = today
            vote.save()
            return Response({'detail': 'Your vote has been updated'}, status=status.HTTP_200_OK)

        except Vote.DoesNotExist:
            # Якщо не голосував, створюємо новий запис
            Vote.objects.create(user=user, choice=choice)
            return Response({'detail': 'Your vote has been recorded'}, status=status.HTTP_201_CREATED)


class ResultView(generics.ListAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        today_menu = Menu.objects.filter(date=date.today()).first()
        return Vote.objects.filter(menu=today_menu)

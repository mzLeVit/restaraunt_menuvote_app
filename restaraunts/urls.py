
from django.urls import path
from .views import RestaurantCreateView, MenuCreateView, TodayMenuView, ResultView, CheckVoteView, VoteView

urlpatterns = [
    path('restaurants/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('menu/', MenuCreateView.as_view(), name='menu-create'),
    path('menu/today/', TodayMenuView.as_view(), name='menu-today'),
    path('vote/', VoteView.as_view(), name='vote'),
    path('results/', ResultView.as_view(), name='results'),
    path('api/check-vote/', CheckVoteView.as_view(), name='check-vote'),
    path('api/vote/', VoteView.as_view(), name='vote'),
]

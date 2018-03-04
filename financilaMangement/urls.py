# _author : litufu
# date : 2018/3/4
from django.urls import path

from . import views

urlpatterns = [
    # ex: /financilaMangement/
    path('', views.index, name='index'),
    # ex: /financilaMangement/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /financilaMangement/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /financilaMangement/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
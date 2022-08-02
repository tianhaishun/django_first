# -*- coding:utf-8 -*-
# @Time : 8/1/2022 10:56 AM 
# @Author : haistian
# @File : urls.py 
# @Software: PyCharm
from django.urls import path
from .import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:quesiton_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.results, name='vote'),
    # added the word 'specifics'
    path('specifics/<int:question_id>/', views.detail, name='detail'),
]

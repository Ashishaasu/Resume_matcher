from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_view, name='match-view'),
]

from django.urls import path
from .views import word_view, meaning_view

urlpatterns = [
    path('word/<str:query>/', word_view, name='word_view'),
    path('meaning/<str:query>/', meaning_view, name='meaning_view'),
]

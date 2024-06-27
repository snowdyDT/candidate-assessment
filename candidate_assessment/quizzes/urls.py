from django.urls import path

from quizzes import views

urlpatterns = [
    path('', views.index),
    path('types/<int:types_id>/', views.types),
    path('types/<slug:types_slug>/', views.types_by_slug),
]

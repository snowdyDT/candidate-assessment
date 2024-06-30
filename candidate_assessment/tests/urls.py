from django.urls import path
from . import views

urlpatterns = [
    path('test/<int:test_id>/', views.take_test, name='take_test'),
    path('test/<int:test_id>/result/', views.test_result, name='test_result'),
]

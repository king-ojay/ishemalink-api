from django.urls import path
from .views import APIRootView, HealthCheckView

urlpatterns = [
    path('', APIRootView.as_view()),
    path('status/', HealthCheckView.as_view()),
]

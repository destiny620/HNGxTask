from django.urls import path
from .views import get_slack_details

urlpatterns = [
    path('api', get_slack_details, name="get_slack_details")
]
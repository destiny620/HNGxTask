from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from endpointapp.serializers import SlackSerializer
import datetime


# Create your views here.

@api_view(['GET'])
def get_slack_details(request):
    """Enpoint returns preformatted data"""

    current_datetime = datetime.datetime.now()
    day_of_week = current_datetime.weekday()
    day_name = current_datetime.strftime('%A')

    # UTC Formatting to precision of +/-2 minute
    # now = datetime.datetime.utcnow()
    # utc_timezone = pytz.timezone("UTC")
    # current_utc_time = utc_timezone.localize(now)
    current_utc_time = datetime.datetime.utcnow()
    formatted_utc_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    slack_name = request.query_params.get('slack_name')
    track = request.query_params.get('track')
    current_day = day_name
    github_file_url = "https://github.com/JosephJohncross/HNGX_stage_one/blob/main/endpoint_intro/views.py"
    github_repo_url = "https://github.com/JosephJohncross/HNGX_stage_one"
    status_code = 200
    utc_time = formatted_utc_time

    # slack_name: slack_name,
    # current_day: current_day,

    data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': status_code
    }

    serializer = SlackSerializer(data=data)

    if serializer.is_valid():
        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



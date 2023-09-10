# from django.db.models import fields
from rest_framework import serializers
from .models import Endpoint



class EndpointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endpoint
		fields = ('slack_name', 'current_day', 'utc_time', 'track', 'github_file_url', 'gitup_repo_url', 'status_code')
		

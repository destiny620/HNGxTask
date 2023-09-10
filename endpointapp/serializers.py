from rest_framework import serializers




# class EndpointSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Endpoint
# 		fields = ('slack_name', 'current_day', 'utc_time', 'track', 'github_file_url', 'gitup_repo_url', 'status_code')
		
class SlackSerializer(serializers.Serializer):
    """Serializes slack formatted output"""

    slack_name = serializers.CharField()
    current_day = serializers.CharField()
    utc_time = serializers.DateTimeField()
    track = serializers.CharField()
    github_file_url = serializers.CharField()
    github_repo_url = serializers.CharField()
    status_code = serializers.IntegerField()
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Endpoint
from .serializers import EndpointSerializer
from rest_framework import status
from datetime import date
import calendar

# Create your views here.



@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': 'all',
		'Search by Slack': '/?slack_name=slack_name',
		'Search by Track': '/?track=track',
	}

	return Response(api_urls)

    
@api_view(['GET'])
def view_items(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = Endpoint.objects.filter(**request.query_params.dict())
       
    else:
        items = Endpoint.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = EndpointSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Endpoint
from .serializers import EndpointSerializer
from rest_framework import status
from django.urls import reverse


# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
      # checking for the parameters from the URL
    if request.query_params:
        items = Endpoint.objects.filter(**request.query_params.dict())
       
    else:
        items = Endpoint.objects.all()
 
    # if there is something in items else raise error
    # if items:
        serializer = EndpointSerializer(items, many=True)
        return Response(serializer.data)
    # else:
    #     print("No Items Found")
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
     
#  @api_view(['GET', 'POST'])
# def track_list(request):
#     """
#     View and Create Post.
#     """
#     if request.method == 'GET':
#         tracks = Track.objects.all()
       
#         serializer = TrackSerializer(tracks, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def view_items(request):
#     api_urls = {
#         'all_items': '/',
# 		'Search by Slack': '/?slack_name=slack_name',
# 		'Search by Track': '/?track=track',
# 	}

#     return Response(api_urls)

@api_view(['GET'])
def view_items(request):
    api_urls = {
        'all_items': reverse('home'),
        'Search by Slack': f"{reverse('home')}?slack_name=slack_name",
        'Search by Track': f"{reverse('home')}?track=track",
    }

    return Response(api_urls)

     
  
    


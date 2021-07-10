from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
# NOTE:     'Test API View'
    def get(self, request, format=None):
        """Returns a list of API View features"""
        an_apiview  = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!!!', 'an_apiview' : an_apiview})
# Create your views here

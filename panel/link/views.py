from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from ..link.models import Link


class LinkView(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        try:
            links = Link.objects.filter(is_active=True)
            print(links)
            return Response(links, status=status.HTTP_200_OK)
        except:
            return Response("Something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)
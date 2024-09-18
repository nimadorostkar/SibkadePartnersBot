from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from link.models import Link


class LinkView(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        try:
            links = Link.objects.filter(is_active=True)
            data = {}
            for link in links:
                type = link.type
                duration = link.duration
                if type not in data:
                    data[type] = {}
                data[type][duration] = {
                    "code": link.code,
                    "link": link.link}
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response("Something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)
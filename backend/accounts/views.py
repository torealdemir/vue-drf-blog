from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view


class RegisterView(APIView):
    # permission_classes = permissions.AllowAny
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

@api_view(['POST'])
def RegisterApiView():
    permission_classes = [permissions.AllowAny]

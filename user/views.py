from django.contrib.auth import logout
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.test import APIClient
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer, UserRegisterSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegistrationView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        data = {'token': token.key}
        return Response(data=data, status=status.HTTP_200_OK)


# class LoginView(APIView):
#     serializer_class = AuthTokenSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = User.objects.get(email=request.data.get('username'))
#         token = Token.objects.get(user=user).key
#         data = {'token': token}
#         # client = APIClient()
#         # client.login(username=user.email, password=user.password)
#         return Response(data=data)

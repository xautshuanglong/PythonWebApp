
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserInfo
from .serializers import UserInfoSerializer


class UserInfoList(APIView):
    def get(self, request, format=None):
        user_list = UserInfo.objects.all()
        user_list_serializer = UserInfoSerializer(user_list, many=True)
        return Response(user_list_serializer.data)

    def post(self, request, format=None):
        return Response("UserInfoList")


class UserInfoOne(APIView):
    def get(self, request, id, format=None):
        try:
            response_str = ""
            user = UserInfo.objects.get(id=id)
            user_serializer = UserInfoSerializer(user, many=False)
            return Response(user_serializer.data)
        except UserInfo.DoesNotExist:
            return Response("Not Found")

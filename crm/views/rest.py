from rest_framework.views import APIView
from rest_framework.response import Response
from crm.serializers import ProfileSerializer


class ProfileRest(APIView):
    ser = ProfileSerializer

    def get(self, request, *args, **kwargs):
        ser_data = self.ser(request.user)
        return Response(ser_data.data)
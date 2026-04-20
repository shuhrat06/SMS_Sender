from .serializer import SmsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SendSMSView(APIView):
    def post(self, request):
        serializer = SmsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


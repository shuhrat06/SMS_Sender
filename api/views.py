from .serializer import SmsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NewSms

class SendSMSView(APIView):
    def post(self, request):
        serializer = SmsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendSeveralSMSView(APIView):
    def post(self, request):
        data = request.data
        smss = []
        for i in data:
            try:
                smss.append(NewSms(
                    phone = i.get('phone'),
                    msg = i.get('msg')
                ))
            except:
                print('--NewSms obyekt yaratilmadi...')
        if smss:
            NewSms.objects.bulk_create(smss)
        return Response(status=status.HTTP_200_OK)


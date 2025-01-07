from django.shortcuts import render
from rest_framework import viewss, response,status

# Create your views here.

class WebhooksOrderView(viewss.APIView):
    def post(self, request):
        data=request.data
        return response.Response(
            data=data,
            status= status.HTTP_200_OK
        )
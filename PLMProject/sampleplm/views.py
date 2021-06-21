from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
import json
from rest_framework import viewsets
# Create your views here.

from .models import plmProcessTracking, PlmProcessResponse
from .serializers import *
import configparser



@api_view(['GET', 'POST'])
def plmProcessing(request, *args, **kwargs):
    """
        Create the queued data record
    """
    if kwargs.get("server", None) is not None:
        server = kwargs["server"]

    if kwargs.get("stage", None) is not None:
        stage = kwargs["stage"]

    if kwargs.get("stage", None) is not None:
        step = kwargs["step"]

    print('before the get method')

    if request.method == 'GET':

        parser = configparser.ConfigParser()
        config_file = "D:\DanteLearn\django-projects\PLM\PLMProject\sampleplm\config_file.ini"
        parser.read(config_file)
        # func = parser["Step1"]["function"]
        # print(func('Dante'))
        plmProcess = plmProcessTracking.objects.all()
        serializer = plmprocessTrackingSerializer(plmProcess, context={'request': request}, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        print('inside post method')
        servernamein = request.data.get('serverName')
        queryset = plmProcessTracking.objects.filter(serverName=servernamein)
        if queryset:
            plmid = plmProcessTracking.objects.get(serverName=servernamein)
            print(plmid.id)
            if plmid:
                # plmProcessObj = plmProcessTracking.objects.get(plmProcessTracking__pk=queryset.id)
                responsemodel = {
                    'id' : '1116',
                    'plmStep' : step,
                    'response' : 'Initial Response2',
                    'plm' : plmid.id
                }
                serializer = plmProcessResponseSerializer(data=responsemodel)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            plmProcess = plmProcessTracking.objects.all()
            request.data['plmStep'] = step
            
            serializer = plmprocessTrackingSerializer(data=request.data)
            print('serializer invoked')
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class listPlmViewset(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        print('Inside the list function of viewset')
        queryset = plmProcessTracking.objects.all()
        serializer = plmprocessTrackingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = plmProcessTracking.objects.all()
        user = get_object_or_404(queryset, serverName=pk)
        serializer = plmprocessTrackingSerializer(user)
        return Response(serializer.data)


def function_called(text):
    return 'function called invoked with ' + text
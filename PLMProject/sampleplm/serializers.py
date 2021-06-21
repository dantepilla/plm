from rest_framework import serializers
from .models import plmProcessTracking, PlmProcessResponse


class plmProcessResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlmProcessResponse
        fields = ('id','plmStep', 'response', 'plm')


class plmprocessTrackingSerializer(serializers.ModelSerializer):

    # responses = plmProcessResponseSerializer(many=True)
    
    class Meta:
        model = plmProcessTracking
        # fields = ('id','serverName', 'plmStatus', 'changeNumber', 'plmStep' )
        fields = '__all__'        

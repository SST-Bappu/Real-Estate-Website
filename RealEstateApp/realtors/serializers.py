from rest_framework import fields, serializers
from .models import realtors

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = realtors
        fields ='__all__'
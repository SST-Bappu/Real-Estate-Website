from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import realtors
from .serializers import RealtorSerializer
# Create your views here.

class RealtorListView(ListAPIView):
    permission_classes= (permissions.AllowAny,)
    queryset = realtors.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None

class RealtorView(RetrieveAPIView):
    queryset = realtors.objects.all()
    serializer_class = RealtorSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = realtors.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None
from urllib.request import Request

from django.db.models import Count, Avg, Min, Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from shoes.models import Shoe
from .serializers import ShoeSerializer, ShoeNestedReadSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ReadWriteSerializerMixin:
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.read_serializer
        return self.write_serializer


class ShoeListCreateAPIView(ReadWriteSerializerMixin, ListCreateAPIView):
    queryset = Shoe.objects.prefetch_related('reviews').all()
    permission_classes = [IsAdminOrReadOnly]

    read_serializer = ShoeNestedReadSerializer
    write_serializer = ShoeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['category', 'gender']
    search_fields = ['name', 'brand']
    ordering_fields = ['price']

class ShoeDetailAPIView(ReadWriteSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.prefetch_related('reviews').all()

    read_serializer = ShoeNestedReadSerializer
    write_serializer = ShoeSerializer

class ShoeStatsView(APIView):
    def get(self, request: Request):
        stats = Shoe.objects.aggregate(
            total_shoes=Count('id'),
            avg_price=Avg('price'),
            min_price=Min('price'),
            max_price=Max('price'),
        )
        return Response(stats)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Shoe
from .serializers import ShoeSerializer, ShoeNestedReadSerializer


class ReadWriteSerializerMixin:
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.read_serializer
        return self.write_serializer


class ShoeListCreateAPIView(ReadWriteSerializerMixin, ListCreateAPIView):
    queryset = Shoe.objects.prefetch_related('reviews').all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    read_serializer = ShoeNestedReadSerializer
    write_serializer = ShoeSerializer

class ShoeDetailAPIView(ReadWriteSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.prefetch_related('reviews').all()

    read_serializer = ShoeNestedReadSerializer
    write_serializer = ShoeSerializer
from rest_framework import generics

from text.models import Text
from text.serializers import TextSerializer


class TextView(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class TextDetailView(generics.RetrieveAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

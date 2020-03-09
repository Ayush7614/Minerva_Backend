from rest_framework import serializers
from text.models import Text

class TextSerializer(serializers.ModelSerialier):
    class Meta:
        model = Text
        fields = ['text, image']

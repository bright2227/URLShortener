from rest_framework import serializers
from urlshortener.models import Shortener


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ["id", "long_url"]

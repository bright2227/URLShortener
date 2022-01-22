from base64 import b64decode, b64encode
from django.conf import settings
from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from urlshortener.models import Shortener
from urlshortener.serializers import ShortUrlSerializer


CACHE_DURATION = settings.CACHE_DURATION


class ShortenURLView(ViewSet):
    permission_classes = (AllowAny,)

    def get_orginal_url(self, request, short_url):
        try:
            sh_id = int(b64decode(short_url.encode('utf-8')))
        except:
            return Response("invalid short url", status=status.HTTP_400_BAD_REQUEST)

        sh_long_url = cache.get(sh_id)
        if sh_long_url is not None:
            return Response({'long_url': sh_long_url}, status=status.HTTP_200_OK, content_type='application/json')

        sh = Shortener.objects.get(id=sh_id)
        ser = ShortUrlSerializer(sh)

        long_url = ser.data['long_url']
        cache.set(sh_id, long_url, CACHE_DURATION)
        return Response({'long_url': long_url}, status=status.HTTP_200_OK, content_type='application/json' )

    def shorten_url(self, request):
        serializer = ShortUrlSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        sh = serializer.create(serializer.data)
        cache.set(sh.id, sh.long_url, CACHE_DURATION)
        return Response(
            {'short_url': b64encode(str(sh.id).encode('utf-8'))},
            status=status.HTTP_201_CREATED,
            content_type='application/json'
        )

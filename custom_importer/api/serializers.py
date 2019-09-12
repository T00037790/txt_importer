from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    files = serializers.FileField(required=True)



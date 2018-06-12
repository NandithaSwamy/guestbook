from rest_framework import serializers

class Getserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    comment = serializers.CharField()

class Postserializer(serializers.Serializer):
    name = serializers.CharField()
    comment = serializers.CharField()


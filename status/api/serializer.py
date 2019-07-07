from rest_framework import serializers

from status.models import Status


class ListSerializers(serializers.ModelSerializer):


    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image',
            'timestamp',
            'updated'
        ]

from .models    import TimestampModel
from rest_framework  import serializers


class TimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimestampModel
        fields = ('created_at', 'updated_at')
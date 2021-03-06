from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
<<<<<<< HEAD
        if data.get('status', '') not in ('CLOSED', 'DRAFT') and self.context["request"].method == 'POST':
=======
        if data.get('status', '') not in ('CLOSED', 'DRAFT') or self.context["request"].method == 'POST':
>>>>>>> 3fac880ae731da1208675d2da5b0ea1a741cbb44
            if Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN').count() > 10:
                raise serializers.ValidationError("You cannot create more then 10 advert with OPEN status")
        return data

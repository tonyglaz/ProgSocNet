from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """ Вывод инфо о UserNet"""

    class Meta:
        model = UserNet
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser")

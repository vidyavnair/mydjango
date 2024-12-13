from rest_framework import serializers
from .models import Full_data


class Full_data_serializers(serializers.ModelSerializer):

    class Meta:
        model=Full_data
        fields='__all__'
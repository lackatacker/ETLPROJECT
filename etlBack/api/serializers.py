from rest_framework import serializers
from .models import Transaction, TransformationBlock


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransformationBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransformationBlock
        fields = '__all__'

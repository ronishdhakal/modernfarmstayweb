# review/serializers.py
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_star(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Star must be between 1 and 5.")
        return value

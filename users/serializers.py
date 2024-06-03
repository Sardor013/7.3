import validators
from rest_framework import serializers

from .models import User, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, date):
        if date['username'].isalnum():
            return date

        raise serializers.ValidationError({'username': 'Name must be alphanumeric'})

    def validate_first_name(self, date):
        if any(i.isdigit() for i in date):
            raise serializers.ValidationError("In First name don't have numbers")
        return date

    def validate_last_name(self, date):
        if any(i.isdigit() for i in date):
            raise serializers.ValidationError("In Last name don't have numbers")
        return date

    def validate_email(self, date):
        if validators.email(date):
            return date
        raise serializers.ValidationError('Email not valid')

    def validate_phone(self, date):
        if date.startswith('+998') and len(date) < 14:
            return date
        raise serializers.ValidationError('Phone not valid')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'











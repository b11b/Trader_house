from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    
    def validate_name(self, value):
        if not value.strip():
            raise ValidationError("Bad name. Not more than 5 symbols and without spaces")
        
        if len(value) > 8:
            raise ValidationError("Bad name. Not more than 5 symbols and without spaces.")

        if ' ' in value:
            raise ValidationError("Bad name. Name can't contain spaces.")

        if User.objects.filter(name=value).exists():
            raise ValidationError(f'User with name {value} exsits')
        
        return value
    class Meta:
        model = User
        fields = ['id', 'name']
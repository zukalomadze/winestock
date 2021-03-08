from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # def clean_password2(self):
    #     password = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password and password2 and password != password2:
    #         raise ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     return password2
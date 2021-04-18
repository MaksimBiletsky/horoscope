from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'date_of_birth', 'password', 'password2']

    def save(self, **kwargs):
        print(self.validated_data)
        if self.validated_data['user']['password'] != self.validated_data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        user = User(
            email=self.validated_data['user']['email'],
            username=self.validated_data['user']['username'],
            password=self.validated_data['user']['password'],
        )
        user.save()
        user_profile = UserProfile(user=user,
                                   date_of_birth=self.validated_data['date_of_birth'])
        user_profile.save()
        return user_profile
#
# class RegisterSerializer(serializers.ModelSerializer):
#
#     email = serializers.DateField(source='user.email')
#     username = serializers.DateField(source='user.username')
#     password = serializers.DateField(source='user.password', write_only=True)
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = UserProfile
#         fields = ['email', 'username', 'date_of_birth', 'password', 'password2']
#
#     def save(self, **kwargs):
#         if self.validated_data['password'] != self.validated_data['password2']:
#             raise serializers.ValidationError({'password': 'Passwords must match!'})
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#             password=self.validated_data['password'],
#         )
#         user.save()
#         user_profile = UserProfile(user=user,
#                                    date_of_birth=self.validated_data['date_of_birth'])
#         user_profile.save()
#         return user_profile

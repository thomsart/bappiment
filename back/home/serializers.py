from rest_framework import serializers

from .models import CustomUser, CustomUserStatus, Membership



########### USER STATUS #######################################################
########### USER STATUS #######################################################
########### USER STATUS #######################################################

class CustomUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserStatus
        fields = ['url', 'status']

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['url', 'user', 'status']

########### USER ##############################################################
########### USER ##############################################################
########### USER ##############################################################

class LightCustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone']

class HeavyCustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']
        # days_off, days_off_cumul, permanent_contract

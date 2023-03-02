from rest_framework import serializers

from .models import User, UserStatus, Membership



########### USER STATUS #######################################################
########### USER STATUS #######################################################
########### USER STATUS #######################################################

class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ["url", "status"]

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["url", "user", "status"]

########### USER ##############################################################
########### USER ##############################################################
########### USER ##############################################################

class LightUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone"]

class HeavyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone",
                  "days_off", "days_off_cumul", "permanent_contract"]

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "password"]


# {
# "first_name": "Marc",
# "last_name": "Touati",
# "email":"mt@gmail.com",
# "phone": "0646756938",
# "password": "tatayoyo77+"
# }
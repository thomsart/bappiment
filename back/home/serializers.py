from rest_framework import serializers

from .models import CustomUser, Status, Membership
from .forms import CustomUserCreationForm
from .managers import CustomUserManager



########### STATUS #######################################################


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name"]


########### USER #########################################################


class LightCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "phone"]


class HeavyCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "phone",
                  "days_off", "days_off_cumul", "permanent_contract"]


class CreateCustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):

        user = CustomUser.objects.create_user(**validated_data)

        return user

# {
# "email": "nanard@gmail.com",
# "first_name": "Bernard",
# "last_name": "Delb",
# "phone": "0646756938",
# "password": "thebigboss77570+"
# }

########### MEMBERSHIP ###################################################


class MembershipSerializer(serializers.ModelSerializer):
    user = LightCustomUserSerializer()
    status = StatusSerializer()
    class Meta:
        model = Membership
        fields = ["id", "user", "status", "date"]


class CreateMembershipSerializer(serializers.Serializer):
    user = LightCustomUserSerializer()
    status = StatusSerializer()

    def to_internal_value(self, data):

        user = data.get('user')
        status = data.get('status')

        # Perform the data validation.
        if not user:
            raise serializers.ValidationError({
                'user': 'This field is required.'
            })
        if not status:
            raise serializers.ValidationError({
                'status': 'This field is required.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'user': CustomUser.objects.get(id=user["id"]),
            'status': Status.objects.get(id=status["id"])
        }

    def create(self, validated_data):

        membership = Membership.objects.create(**validated_data)
        membership.save()

        user = validated_data['user']
        status = validated_data['status']
        if int(user.hightest_level) < int(status.level):
            user.hightest_level = status.level

        return MembershipSerializer(membership)

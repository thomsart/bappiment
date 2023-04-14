from rest_framework import serializers

from .models import CustomUser, Status, Membership
from .forms import CustomUserCreationForm
from .managers import CustomUserManager



########### STATUS #######################################################

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name", "level"]


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
    status = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):

        status_name = validated_data.pop("status")
        status = Status.objects.get(name=status_name)
        user = CustomUser.objects.create_user(**validated_data)

        if user:
            user.hightest_level = status.level
            user.save()
            Membership.objects.create(user=user, status=status)

            return user

# {
# "email": "bd@gmail.com",
# "first_name": "Bernard",
# "last_name": "Delb",
# "phone": "0646756943",
# "password": "thebigboss77+",
# "status": "patron"
# }

# {
# "email": "george@gmail.com",
# "first_name": "George",
# "last_name": "McFly",
# "phone": "0646756943",
# "password": "2virgule21gigawatt+",
# "status": "électrotechnicien"
# }

# {
# "email": "nat@gmail.com",
# "first_name": "Nathalie",
# "last_name": "McFly",
# "phone": "0646756944",
# "password": "tatayoyo77+",
# "status": "comptable"
# }

class UpdateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone", "permanent_contract"]

########### MEMBERSHIP ###################################################

class MembershipSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    user = LightCustomUserSerializer()

    class Meta:
        model = Membership
        fields = ["id", "status", "user", "date"]


class CreateMembershipSerializer(serializers.Serializer):
    status = StatusSerializer()
    user = LightCustomUserSerializer()

# {
#     "user": {
#         "id": 3,
#         "first_name": "Bernard",
#         "last_name": "Delb",
#         "phone": "0646756938"
#     },
#     "status": {
#         "name": "patron"
#     }
# }

# {
#     "user":
#         {
#             "id": 4,
#             "first_name": "Julie",
#             "last_name": "Perin",
#             "phone": "0646756939"
#         },
#     "status":
#         {
#             "name": "comptable"
#         }
# }

# {
#     "user":
#         {
#             "id": 9,
#             "first_name": "George",
#             "last_name": "McFly",
#             "phone": "0646756943"
#         },
#     "status":
#         {
#             "name": "comptable"
#         }
# }

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
            'status': Status.objects.get(name=status["name"])
        }

    def create(self, validated_data):

        membership = Membership.objects.create(**validated_data)
        membership.save()

        user = CustomUser.objects.get(id=validated_data["user"].id)
        status = Status.objects.get(name=validated_data["status"].name)
        if int(user.hightest_level) < int(status.level):
            user.hightest_level = status.level
            user.save()

        return MembershipSerializer(membership)

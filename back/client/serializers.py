from rest_framework import serializers

from .models import LegalEntity, Client, Installation


########### LEGAL ENTITIES ####################################################

class LegalEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntity
        fields = ['name']


########### CLIENT ############################################################

class LightClientSerializer(serializers.ModelSerializer):
    legal_entity = LegalEntitySerializer()
    class Meta:
        model = Client
        fields = ['legal_entity', 'name', 'nb_street', 'street', 'zip_code', 'city',
                  'country', 'contact']


class HeavyClientSerializer(serializers.ModelSerializer):
    legal_entity = LegalEntitySerializer()
    class Meta:
        model = Client
        fields = ['legal_entity', 'name', 'siren', 'siret', 'nb_street', 'street',
                  'zip_code', 'city', 'country', 'date', 'contact']


class CreateClientSerializer(serializers.ModelSerializer):
    legal_entity = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=50)
    siren = serializers.CharField(max_length=9)
    siret = serializers.CharField(max_length=14)
    nb_street = serializers.CharField(max_length=10)
    street = serializers.CharField(max_length=50)
    zip_code = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=20)

    def create(self, validated_data):

        legal_entity = LegalEntity.objects.get(entity=validated_data["legal_entity"])
        if legal_entity:
            validated_data['legal_entity'] = legal_entity.pk
            client = Client.objects.create(**validated_data)
            client.save()

            return client


class UpdateClientSerializer(serializers.ModelSerializer):
    ...


########### INSTALLATION ######################################################

class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'
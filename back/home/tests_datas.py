from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse_lazy

from .models import User, UserStatus, Membership



class HomeAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """ Creation of all users' types. """
        
        # We create normals user
        cls.boss = User.objects.create(
            first_name="Bernard", last_name="Delb", username="nanard@gmail.com",
            email="nanard@gmail.com", phone="0646523895", password="berndelb3895+")
        cls.accountant = User.objects.create(
            first_name="Catherine", last_name="Delb", username="chatdelb@gmail.com",
            email="chatdelb@gmail.com", phone="0646869555", password="chatbelda+/58-")
        cls.hr = User.objects.create(
            first_name="Justine", last_name="Ferrand", username="justfer@gmail.com",
            email="justfer@gmail.com", phone="0675968532", password="jujustf9546+7")
        cls.commercial = User.objects.create(
            first_name="Alan", last_name="Ratenan", username="alan@gmail.com",
            email="alan@gmail.com", phone="0646869532", password="alalnana9958-")
        cls.repair_operator = User.objects.create(
            first_name="Florian", last_name="Bertault", username="foutrien@gmail.com",
            email="foutrien@gmail.com", phone="0785968537", password="foufouf94*6+1")
        cls.receptionist = User.objects.create(
            first_name="Magalie", last_name="Bardo", username="magbar@gmail.com",
            email="magbar@gmail.com", phone="0756368537", password="mabar455446+1")
        cls.stock_operator = User.objects.create(
            first_name="Fabien", last_name="Cottenceau", username="fabiche@gmail.com",
            email="fabiche@gmail.com", phone="0656364447", password="bichon1a*-5+1")
        cls.electrotechnician = User.objects.create(
            first_name="Frédéric", last_name="Souris", username="fredsouris@gmail.com",
            email="fredsouris@gmail.com", phone="0756364578", password="thebest8554*-")
        cls.repairman = User.objects.create(
            first_name="Gérald", last_name="Travers", username="gegetra@gmail.com",
            email="gegetra@gmail.com", phone="0756345712", password="tuning48554*-")
        cls.coppersmith = User.objects.create(
            first_name="Patrice", last_name="Duarte", username="patoche@gmail.com",
            email="patoche@gmail.com", phone="0556222712", password="teenager554/+")
        cls.locksmith = User.objects.create(
            first_name="Mathieu", last_name="Léaute", username="mamat@gmail.com",
            email="mamat@gmail.com", phone="0556333712", password="512arnac784-*")
        cls.mason = User.objects.create(
            first_name="Thierry", last_name="Gréco", username="titigreco@gmail.com",
            email="titigreco@gmail.com", phone="0542983712", password="leraleure/78*")
        cls.postman = User.objects.create(
            first_name="Samy", last_name="Leblanc", username="samyleblanc@gmail.com",
            email="samyleblanc@gmail.com", phone="0542983759", password="larnaque*-78*")
        cls.installer = User.objects.create(
            first_name="Thomas", last_name="Cottenceau", username="totococo@gmail.com",
            email="totococo@gmail.com", phone="0642973752", password="tatayoyo77+")
        cls.maintenance_agent = User.objects.create(
            first_name="Christophe", last_name="Colombel", username="christobale@gmail.com",
            email="christobale@gmail.com", phone="0756986532", password="thebuze784/")
        cls.client = User.objects.create(
            first_name="Mireille", last_name="Marçeau", username="mimimar@gmail.com",
            email="mimimar@gmail.com", phone="0645856912", password="mimi/mars8-")

        # specific user
        cls.user_not_active = User.objects.create(
            first_name="Pierre", last_name="Pas actif", username="pipiinactif@gmail.com",
            email="pipiinactif@gmail.com", phone="0648569745", password="kjefo4ars8-",
            is_active=False)































        # variables for test
        cls.url_user_list = reverse_lazy('users-list')
        cls.url_user_detail = reverse_lazy('users-detail')
        cls.con_user = APIClient()
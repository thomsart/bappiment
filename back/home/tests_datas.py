from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse_lazy

from .models import User, Status, Membership



class HomeAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """ Creation of all users' types. """

        # We create all status

        cls.status_boss = Status.objects.create(name="boss")
        cls.status_accountant = Status.objects.create(name="accountant")
        cls.status_hr = Status.objects.create(name="hr")
        cls.status_commercial = Status.objects.create(name="commercial")
        cls.status_repair_operator = Status.objects.create(name="repair_operator")
        cls.status_receptionist = Status.objects.create(name="receptionist")
        cls.status_stock_operator = Status.objects.create(name="stock_operator")
        cls.status_electrotechnician = Status.objects.create(name="electrotechnician")
        cls.status_repairman = Status.objects.create(name="repairman")
        cls.status_coppersmith = Status.objects.create(name="coppersmith")
        cls.status_locksmith = Status.objects.create(name="locksmith")
        cls.status_mason = Status.objects.create(name="mason")
        cls.status_postman = Status.objects.create(name="postman")
        cls.status_installer = Status.objects.create(name="installer")
        cls.status_maintenance_agent = Status.objects.create(name="maintenance_agent")
        cls.status_client = Status.objects.create(name="client")

        # We create normals user

        cls.user_boss = User.objects.create(
            first_name="Bernard", last_name="Delb", username="nanard@gmail.com",
            email="nanard@gmail.com", phone="0646523895", password="berndelb3895+")
        cls.membership_boss = Membership.objects.create(
            user=cls.user_boss, status=cls.status_boss)

        cls.user_accountant = User.objects.create(
            first_name="Catherine", last_name="Delb", username="chatdelb@gmail.com",
            email="chatdelb@gmail.com", phone="0646869555", password="chatbelda+/58-")
        cls.membership_accountant = Membership.objects.create(
            user=cls.user_accountant, status=cls.status_boss)

        cls.user_hr = User.objects.create(
            first_name="Justine", last_name="Ferrand", username="justfer@gmail.com",
            email="justfer@gmail.com", phone="0675968532", password="jujustf9546+7")
        cls.membership_hr = Membership.objects.create(
            user=cls.user_hr, status=cls.status_hr)

        cls.user_commercial = User.objects.create(
            first_name="Alan", last_name="Ratenan", username="alan@gmail.com",
            email="alan@gmail.com", phone="0646869532", password="alalnana9958-")
        cls.membership_commercial = Membership.objects.create(
            user=cls.user_commercial, status=cls.status_commercial)

        cls.user_repair_operator = User.objects.create(
            first_name="Florian", last_name="Bertault", username="foutrien@gmail.com",
            email="foutrien@gmail.com", phone="0785968537", password="foufouf94*6+1")
        cls.membership_repair_operator = Membership.objects.create(
            user=cls.user_repair_operator, status=cls.status_repair_operator)

        cls.user_receptionist = User.objects.create(
            first_name="Magalie", last_name="Bardo", username="magbar@gmail.com",
            email="magbar@gmail.com", phone="0756368537", password="mabar455446+1")
        cls.membership_repair_operator = Membership.objects.create(
            user=cls.user_receptionist, status=cls.status_receptionist)

        cls.user_stock_operator = User.objects.create(
            first_name="Fabien", last_name="Cottenceau", username="fabiche@gmail.com",
            email="fabiche@gmail.com", phone="0656364447", password="bichon1a*-5+1")
        cls.membership_stock_operator = Membership.objects.create(
            user=cls.user_stock_operator, status=cls.status_stock_operator)

        cls.user_electrotechnician = User.objects.create(
            first_name="Frédéric", last_name="Souris", username="fredsouris@gmail.com",
            email="fredsouris@gmail.com", phone="0756364578", password="thebest8554*-")
        cls.membership_electrotechnician = Membership.objects.create(
            user=cls.user_electrotechnician, status=cls.status_electrotechnician)

        cls.user_repairman = User.objects.create(
            first_name="Gérald", last_name="Travers", username="gegetra@gmail.com",
            email="gegetra@gmail.com", phone="0756345712", password="tuning48554*-")
        cls.membership_repairman = Membership.objects.create(
            user=cls.user_repairman, status=cls.status_repairman)

        cls.user_coppersmith = User.objects.create(
            first_name="Patrice", last_name="Duarte", username="patoche@gmail.com",
            email="patoche@gmail.com", phone="0556222712", password="teenager554/+")
        cls.membership_coppersmith = Membership.objects.create(
            user=cls.user_coppersmith, status=cls.status_coppersmith)

        cls.user_locksmith = User.objects.create(
            first_name="Mathieu", last_name="Léaute", username="mamat@gmail.com",
            email="mamat@gmail.com", phone="0556333712", password="512arnac784-*")
        cls.membership_locksmith = Membership.objects.create(
            user=cls.user_locksmith, status=cls.status_locksmith)

        cls.user_mason = User.objects.create(
            first_name="Thierry", last_name="Gréco", username="titigreco@gmail.com",
            email="titigreco@gmail.com", phone="0542983712", password="leraleure/78*")
        cls.membership_mason = Membership.objects.create(
            user=cls.user_mason, status=cls.status_mason)

        cls.user_postman = User.objects.create(
            first_name="Samy", last_name="Leblanc", username="samyleblanc@gmail.com",
            email="samyleblanc@gmail.com", phone="0542983759", password="larnaque*-78*")
        cls.membership_postman = Membership.objects.create(
            user=cls.user_postman, status=cls.status_postman)

        cls.user_installer = User.objects.create(
            first_name="Thomas", last_name="Cottenceau", username="totococo@gmail.com",
            email="totococo@gmail.com", phone="0642973752", password="tatayoyo77+")
        cls.membership_installer = Membership.objects.create(
            user=cls.user_installer, status=cls.status_installer)

        cls.user_maintenance_agent = User.objects.create(
            first_name="Christophe", last_name="Colombel", username="christobale@gmail.com",
            email="christobale@gmail.com", phone="0756986532", password="thebuze784/")
        cls.membership_maintenance_agent = Membership.objects.create(
            user=cls.user_maintenance_agent, status=cls.status_maintenance_agent)

        cls.user_client = User.objects.create(
            first_name="Mireille", last_name="Marçeau", username="mimimar@gmail.com",
            email="mimimar@gmail.com", phone="0645856912", password="mimi/mars8-")
        cls.membership_client = Membership.objects.create(
            user=cls.user_client, status=cls.status_client)

        # specific user
        cls.user_not_active = User.objects.create(
            first_name="Pierre", last_name="Pas actif", username="pipiinactif@gmail.com",
            email="pipiinactif@gmail.com", phone="0648569745", password="kjefo4ars8-",
            is_active=False)































        # variables for test
        cls.url_user_list = reverse_lazy('users-list')
        cls.url_user_detail = reverse_lazy('users-detail')
        cls.con_user = APIClient()
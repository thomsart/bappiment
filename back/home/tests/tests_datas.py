from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse_lazy

from ..models import CustomUser, Status, Membership
from ..serializers import (
    StatusSerializer, LightCustomUserSerializer, HeavyCustomUserSerializer,
    CreateCustomUserSerializer, MembershipSerializer, CreateMembershipSerializer
)
from ..management.commands.datas import LANGUAGE
from ..management.commands.datas.installation_states import INSTALLATION_STATES
from ..management.commands.datas.product_familys  import PRODUCT_FAMILYS
from ..management.commands.datas.product_states import PRODUCT_STATES
from ..management.commands.datas.user_states  import USER_STATES
from ..management.commands.datas.user_status import STATUS
from ..management.commands.datas.vehicle_states import VEHICLE_STATES



class DatasAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """ Creation of all users' types. """

        ##################### We create all status ############################
        ##################### We create all status ############################
        ##################### We create all status ############################

        cls.status_boss = Status.objects.create(name=STATUS['boss'][LANGUAGE])
        cls.status_accountant = Status.objects.create(name=STATUS['accountant'][LANGUAGE])
        cls.status_hr = Status.objects.create(name="hr")
        cls.status_commercial = Status.objects.create(name=STATUS['commercial'][LANGUAGE])
        cls.status_repair_operator = Status.objects.create(name=STATUS['repair_operator'][LANGUAGE])
        cls.status_receptionist = Status.objects.create(name=STATUS['receptionist'][LANGUAGE])
        cls.status_stock_operator = Status.objects.create(name=STATUS['stock_operator'][LANGUAGE])
        cls.status_electrotechnician = Status.objects.create(name=STATUS['electrotechnician'][LANGUAGE])
        cls.status_repairman = Status.objects.create(name=STATUS['repairman'][LANGUAGE])
        cls.status_coppersmith = Status.objects.create(name=STATUS['coppersmith'][LANGUAGE])
        cls.status_locksmith = Status.objects.create(name=STATUS['locksmith'][LANGUAGE])
        cls.status_mason = Status.objects.create(name=STATUS['mason'][LANGUAGE])
        cls.status_deliveryman = Status.objects.create(name=STATUS['deliveryman'][LANGUAGE])
        cls.status_installer = Status.objects.create(name=STATUS['installer'][LANGUAGE])
        cls.status_maintenance_agent = Status.objects.create(name=STATUS['maintenance_agent'][LANGUAGE])
        cls.status_apprentice = Status.objects.create(name=STATUS['apprentice'][LANGUAGE])
        cls.status_client = Status.objects.create(name=STATUS['client'][LANGUAGE])
        cls.status_supplier = Status.objects.create(name=STATUS['supplier'][LANGUAGE])


        ##################### We create all serializers #######################
        ##################### We create all serializers #######################
        ##################### We create all serializers #######################


        cls.status_serializer = StatusSerializer()
        cls.light_user_serializer = LightCustomUserSerializer
        cls.heavy_user_serializer = HeavyCustomUserSerializer()
        cls.create_user_serializer = CreateCustomUserSerializer()
        cls.membership_serializer = MembershipSerializer()
        cls.create_membership_serializer = CreateMembershipSerializer()


        ######################### We create all users #########################
        ######################### We create all users #########################
        ######################### We create all users #########################

        cls.superuser = CustomUser.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com",
            phone="0606060606", password="tfuamy6574-+",
            hightest_level="0", is_superuser=True)

        cls.user_boss = CustomUser.objects.create(
            first_name="Bernard", last_name="Delb", email="nanard@gmail.com",
            phone="0646523895", password="berndelb3895+", hightest_level="5")
        cls.membership_boss = Membership.objects.create(
            user=cls.user_boss, status=cls.status_boss)

        cls.user_accountant = CustomUser.objects.create(
            first_name="Catherine", last_name="Delb", email="chatdelb@gmail.com", 
            phone="0646869555", password="chatbelda+/58-", hightest_level="4")
        cls.membership_accountant = Membership.objects.create(
            user=cls.user_accountant, status=cls.status_accountant)

        cls.user_hr = CustomUser.objects.create(
            first_name="Justine", last_name="Ferrand", email="justfer@gmail.com",
            phone="0675968532", password="jujustf9546+7", hightest_level="4")
        cls.membership_hr = Membership.objects.create(
            user=cls.user_hr, status=cls.status_hr)

        cls.user_commercial = CustomUser.objects.create(
            first_name="Alan", last_name="Ratenan", email="alan@gmail.com",
            phone="0646869532", password="alalnana9958-", hightest_level="4")
        cls.membership_commercial = Membership.objects.create(
            user=cls.user_commercial, status=cls.status_commercial)

        cls.user_repair_operator = CustomUser.objects.create(
            first_name="Florian", last_name="Bertault", email="foutrien@gmail.com",
            phone="0785968537", password="foufouf94*6+1", hightest_level="4")
        cls.membership_repair_operator = Membership.objects.create(
            user=cls.user_repair_operator, status=cls.status_repair_operator)

        cls.user_receptionist = CustomUser.objects.create(
            first_name="Magalie", last_name="Bardo", email="magbar@gmail.com",
            phone="0756368537", password="mabar455446+1", hightest_level="3")
        cls.membership_repair_operator = Membership.objects.create(
            user=cls.user_receptionist, status=cls.status_receptionist)

        cls.user_stock_operator = CustomUser.objects.create(
            first_name="Fabien", last_name="Cottenceau", email="fabiche@gmail.com",
            phone="0656364447", password="bichon1a*-5+1", hightest_level="3")
        cls.membership_stock_operator = Membership.objects.create(
            user=cls.user_stock_operator, status=cls.status_stock_operator)

        cls.user_electrotechnician = CustomUser.objects.create(
            first_name="Frédéric", last_name="Souris", email="fredsouris@gmail.com",
            phone="0756364578", password="thebest8554*-", hightest_level="3")
        cls.membership_electrotechnician = Membership.objects.create(
            user=cls.user_electrotechnician, status=cls.status_electrotechnician)

        cls.user_repairman = CustomUser.objects.create(
            first_name="Gérald", last_name="Travers", email="gegetra@gmail.com",
            phone="0756345712", password="tuning48554*-", hightest_level="3")
        cls.membership_repairman = Membership.objects.create(
            user=cls.user_repairman, status=cls.status_repairman)

        cls.user_coppersmith = CustomUser.objects.create(
            first_name="Patrice", last_name="Duarte", email="patoche@gmail.com",
            phone="0556222712", password="teenager554/+", hightest_level="3")
        cls.membership_coppersmith = Membership.objects.create(
            user=cls.user_coppersmith, status=cls.status_coppersmith)

        cls.user_locksmith = CustomUser.objects.create(
            first_name="Mathieu", last_name="Léaute", email="mamat@gmail.com",
            phone="0556333712", password="512arnac784-*", hightest_level="3")
        cls.membership_locksmith = Membership.objects.create(
            user=cls.user_locksmith, status=cls.status_locksmith)

        cls.user_mason = CustomUser.objects.create(
            first_name="Thierry", last_name="Gréco", email="titigreco@gmail.com",
            phone="0542983712", password="leraleure/78*", hightest_level="3")
        cls.membership_mason = Membership.objects.create(
            user=cls.user_mason, status=cls.status_mason)

        cls.user_deliveryman = CustomUser.objects.create(
            first_name="Samy", last_name="Leblanc", email="samyleblanc@gmail.com",
            phone="0542983759", password="larnaque*-78*", hightest_level="3")
        cls.membership_deliveryman = Membership.objects.create(
            user=cls.user_deliveryman, status=cls.status_deliveryman)

        cls.user_installer = CustomUser.objects.create(
            first_name="Thomas", last_name="Cottenceau", email="totococo@gmail.com",
            phone="0642973752", password="tatayoyo77+", hightest_level="3")
        cls.membership_installer = Membership.objects.create(
            user=cls.user_installer, status=cls.status_installer)

        cls.user_maintenance_agent = CustomUser.objects.create(
            first_name="Christophe", last_name="Colombel", email="christobale@gmail.com",
            phone="0756986532", password="thebuze784/", hightest_level="3")
        cls.membership_maintenance_agent = Membership.objects.create(
            user=cls.user_maintenance_agent, status=cls.status_maintenance_agent)

        cls.user_apprentice = CustomUser.objects.create(
            first_name="Julien", last_name="Malou", email="apprentice@gmail.com",
            phone="0645856912", password="noksvg5g5n/mars8-", hightest_level="2")
        cls.membership_apprentice = Membership.objects.create(
            user=cls.user_apprentice, status=cls.status_apprentice)

        cls.user_client = CustomUser.objects.create(
            first_name="Mireille", last_name="Marçeau", email="mimimar@gmail.com",
            phone="0645856912", password="mimi/mars8-", hightest_level="1")
        cls.membership_client = Membership.objects.create(
            user=cls.user_client, status=cls.status_client)

        cls.user_supplier = CustomUser.objects.create(
            first_name="Frederic", last_name="Jaegge", email="supplier@gmail.com",
            phone="0645856912", password="noksvg5g5n/mars8-", hightest_level="1")
        cls.membership_supplier = Membership.objects.create(
            user=cls.user_supplier, status=cls.status_supplier)

        # specific user

        cls.user_active = CustomUser.objects.create(
            first_name="Pierre", last_name="Active", email="active@gmail.com",
            phone="0648569745", password="mjefo4ars9-")

        cls.user_not_active = CustomUser.objects.create(
            first_name="Pierre", last_name="Not active",email="notactive@gmail.com",
            phone="0648569745", password="kjefo4ars8-",
            is_active=False, hightest_level="4")

        cls.user_employed = CustomUser.objects.create(
            first_name="Pierre", last_name="Permanent", email="employed@gmail.com",
            phone="0648569745", password="mjefo4ars14-",)

        cls.user_not_employed = CustomUser.objects.create(
            first_name="Pierre", last_name="Not_permanent", email="notemployed@gmail.com",
            phone="0648569745", password="kjefo4ars15-", permanent_contract=False)


        ######################## We create all variables ######################
        ######################## We create all variables ######################
        ######################## We create all variables ######################

        cls.url_status_list = reverse_lazy('status-list')
        cls.url_users_list = reverse_lazy('users-list')
        cls.url_users_detail = 'users-detail'
        cls.url_memberships_list = reverse_lazy('memberships-list')
        cls.url_memberships_detail = 'memberships-list'
        cls.con_user = APIClient()
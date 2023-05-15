from rest_framework.test import APITestCase, APIClient
from django.urls import reverse_lazy

from ..models import LegalEntity, Client, Installation
from home.models import CustomUser, Status, Membership
from home.management.commands.datas import LANGUAGE
from home.management.commands.datas.user_status import STATUS
from home.management.commands.datas.legal_entities  import LEGAL_ENTITIES


class ClientDatasAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """ Creation of all datas. """

        ##################### We create all status ############################
        ##################### We create all status ############################
        ##################### We create all status ############################

        cls.status_boss = Status.objects.create(name=STATUS['boss'][LANGUAGE], level=STATUS['boss']['level'])
        cls.status_accountant = Status.objects.create(name=STATUS['accountant'][LANGUAGE], level=STATUS['accountant']['level'])
        cls.status_hr = Status.objects.create(name=STATUS['hr'][LANGUAGE], level=STATUS['hr']['level'])
        cls.status_commercial = Status.objects.create(name=STATUS['commercial'][LANGUAGE], level=STATUS['commercial']['level'])
        cls.status_repair_operator = Status.objects.create(name=STATUS['repair_operator'][LANGUAGE], level=STATUS['repair_operator']['level'])
        cls.status_receptionist = Status.objects.create(name=STATUS['receptionist'][LANGUAGE], level=STATUS['receptionist']['level'])
        cls.status_stock_operator = Status.objects.create(name=STATUS['stock_operator'][LANGUAGE], level=STATUS['stock_operator']['level'])
        cls.status_electrotechnician = Status.objects.create(name=STATUS['electrotechnician'][LANGUAGE], level=STATUS['electrotechnician']['level'])
        cls.status_repairman = Status.objects.create(name=STATUS['repairman'][LANGUAGE], level=STATUS['repairman']['level'])
        cls.status_coppersmith = Status.objects.create(name=STATUS['coppersmith'][LANGUAGE], level=STATUS['coppersmith']['level'])
        cls.status_locksmith = Status.objects.create(name=STATUS['locksmith'][LANGUAGE], level=STATUS['locksmith']['level'])
        cls.status_mason = Status.objects.create(name=STATUS['mason'][LANGUAGE], level=STATUS['mason']['level'])
        cls.status_deliveryman = Status.objects.create(name=STATUS['deliveryman'][LANGUAGE], level=STATUS['deliveryman']['level'])
        cls.status_cleaner = Status.objects.create(name=STATUS['cleaner'][LANGUAGE], level=STATUS['cleaner']['level'])
        cls.status_installer = Status.objects.create(name=STATUS['installer'][LANGUAGE], level=STATUS['installer']['level'])
        cls.status_maintenance_agent = Status.objects.create(name=STATUS['maintenance_agent'][LANGUAGE], level=STATUS['maintenance_agent']['level'])
        cls.status_apprentice = Status.objects.create(name=STATUS['apprentice'][LANGUAGE], level=STATUS['apprentice']['level'])
        cls.status_client = Status.objects.create(name=STATUS['client'][LANGUAGE], level=STATUS['client']['level'])
        cls.status_supplier = Status.objects.create(name=STATUS['supplier'][LANGUAGE], level=STATUS['supplier']['level'])


        ##################### We create all LegaleEntities ############################
        ##################### We create all LegaleEntities ############################
        ##################### We create all LegaleEntities ############################

        cls.legal_entity_family = LegalEntity.objects.create(name=LEGAL_ENTITIES['family'][LANGUAGE])
        cls.legal_entity_syndic = LegalEntity.objects.create(name=LEGAL_ENTITIES['syndic'][LANGUAGE])
        cls.legal_entity_company = LegalEntity.objects.create(name=LEGAL_ENTITIES['company'][LANGUAGE])
        cls.legal_entity_association = LegalEntity.objects.create(name=LEGAL_ENTITIES['association'][LANGUAGE])
        cls.legal_entity_municipality = LegalEntity.objects.create(name=LEGAL_ENTITIES['municipality'][LANGUAGE])

        ######################### We create all users #########################
        ######################### We create all users #########################
        ######################### We create all users #########################

        cls.superuser = CustomUser.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com",
            phone="0606060606", password="tfuamy6574-+",
            hightest_level="0", is_superuser=True)

        cls.user_boss = CustomUser.objects.create(
            first_name="Bernard", last_name="Delb", email="nanard@gmail.com",
            phone="0646523895", password="berndelb3895+",
            hightest_level=STATUS['boss']['level'])
        cls.membership_boss = Membership.objects.create(
            user=cls.user_boss, status=cls.status_boss)

        cls.user_accountant = CustomUser.objects.create(
            first_name="Catherine", last_name="Delb", email="chatdelb@gmail.com", 
            phone="0646869555", password="chatbelda+/58-",
            hightest_level=STATUS['accountant']['level'])
        cls.membership_accountant = Membership.objects.create(
            user=cls.user_accountant, status=cls.status_accountant)

        cls.user_hr = CustomUser.objects.create(
            first_name="Justine", last_name="Ferrand", email="justfer@gmail.com",
            phone="0675968532", password="jujustf9546+7",
            hightest_level=STATUS['hr']['level'])
        cls.membership_hr = Membership.objects.create(
            user=cls.user_hr, status=cls.status_hr)

        cls.user_commercial = CustomUser.objects.create(
            first_name="Alan", last_name="Ratenan", email="alan@gmail.com",
            phone="0646869532", password="alalnana9958-",
            hightest_level=STATUS['commercial']['level'])
        cls.membership_commercial = Membership.objects.create(
            user=cls.user_commercial, status=cls.status_commercial)

        cls.user_repair_operator = CustomUser.objects.create(
            first_name="Florian", last_name="Bertault", email="foutrien@gmail.com",
            phone="0785968537", password="foufouf94*6+1",
            hightest_level=STATUS['repair_operator']['level'])
        cls.membership_repair_operator = Membership.objects.create(
            user=cls.user_repair_operator, status=cls.status_repair_operator)

        cls.user_receptionist = CustomUser.objects.create(
            first_name="Magalie", last_name="Bardo", email="magbar@gmail.com",
            phone="0756368537", password="mabar455446+1",
            hightest_level=STATUS['receptionist']['level'])
        cls.membership_receptionist = Membership.objects.create(
            user=cls.user_receptionist, status=cls.status_receptionist)

        cls.user_stock_operator = CustomUser.objects.create(
            first_name="Fabien", last_name="Cottenceau", email="fabiche@gmail.com",
            phone="0656364447", password="bichon1a*-5+1",
            hightest_level=STATUS['stock_operator']['level'])
        cls.membership_stock_operator = Membership.objects.create(
            user=cls.user_stock_operator, status=cls.status_stock_operator)

        cls.user_electrotechnician = CustomUser.objects.create(
            first_name="Frédéric", last_name="Souris", email="fredsouris@gmail.com",
            phone="0756364578", password="thebest8554*-",
            hightest_level=STATUS['electrotechnician']['level'])
        cls.membership_electrotechnician = Membership.objects.create(
            user=cls.user_electrotechnician, status=cls.status_electrotechnician)

        cls.user_repairman = CustomUser.objects.create(
            first_name="Gérald", last_name="Travers", email="gegetra@gmail.com",
            phone="0756345712", password="tuning48554*-",
            hightest_level=STATUS['repairman']['level'])
        cls.membership_repairman = Membership.objects.create(
            user=cls.user_repairman, status=cls.status_repairman)

        cls.user_coppersmith = CustomUser.objects.create(
            first_name="Patrice", last_name="Duarte", email="patoche@gmail.com",
            phone="0556222712", password="teenager554/+",
            hightest_level=STATUS['coppersmith']['level'])
        cls.membership_coppersmith = Membership.objects.create(
            user=cls.user_coppersmith, status=cls.status_coppersmith)

        cls.user_locksmith = CustomUser.objects.create(
            first_name="Mathieu", last_name="Léaute", email="mamat@gmail.com",
            phone="0556333712", password="512arnac784-*",
            hightest_level=STATUS['locksmith']['level'])
        cls.membership_locksmith = Membership.objects.create(
            user=cls.user_locksmith, status=cls.status_locksmith)

        cls.user_mason = CustomUser.objects.create(
            first_name="Thierry", last_name="Gréco", email="titigreco@gmail.com",
            phone="0542983712", password="leraleure/78*",
            hightest_level=STATUS['mason']['level'])
        cls.membership_mason = Membership.objects.create(
            user=cls.user_mason, status=cls.status_mason)

        cls.user_deliveryman = CustomUser.objects.create(
            first_name="Samy", last_name="Leblanc", email="samyleblanc@gmail.com",
            phone="0542983759", password="larnaque*-78*",
            hightest_level=STATUS['deliveryman']['level'])
        cls.membership_deliveryman = Membership.objects.create(
            user=cls.user_deliveryman, status=cls.status_deliveryman)
        cls.membership_cleaner = Membership.objects.create(
            user=cls.user_deliveryman, status=cls.status_cleaner)

        cls.user_installer = CustomUser.objects.create(
            first_name="Thomas", last_name="Cottenceau", email="totococo@gmail.com",
            phone="0642973752", password="tatayoyo77+",
            hightest_level=STATUS['installer']['level'])
        cls.membership_installer = Membership.objects.create(
            user=cls.user_installer, status=cls.status_installer)

        cls.user_maintenance_agent = CustomUser.objects.create(
            first_name="Christophe", last_name="Colombel", email="christobale@gmail.com",
            phone="0756986532", password="thebuze784/",
            hightest_level=STATUS['maintenance_agent']['level'])
        cls.membership_maintenance_agent = Membership.objects.create(
            user=cls.user_maintenance_agent, status=cls.status_maintenance_agent)

        cls.user_apprentice = CustomUser.objects.create(
            first_name="Julien", last_name="Malou", email="apprentice@gmail.com",
            phone="0645856912", password="noksvg5g5n/mars8-",
            hightest_level=STATUS['apprentice']['level'])
        cls.membership_apprentice = Membership.objects.create(
            user=cls.user_apprentice, status=cls.status_apprentice)

        cls.user_client = CustomUser.objects.create(
            first_name="Mireille", last_name="Marçeau", email="mimimar@gmail.com",
            phone="0645856912", password="mimi/mars8-",
            hightest_level=STATUS['client']['level'])
        cls.membership_client = Membership.objects.create(
            user=cls.user_client, status=cls.status_client)

        # specific user

        cls.user_active = CustomUser.objects.create(
            first_name="Pierre", last_name="Active", email="active@gmail.com",
            phone="0648569745", password="mjefo4ars9-", hightest_level="3")

        cls.user_not_active = CustomUser.objects.create(
            first_name="Pierre", last_name="Not active",email="notactive@gmail.com",
            phone="0648569745", password="kjefo4ars8-", hightest_level="3",
            is_active=False)

        cls.user_employed = CustomUser.objects.create(
            first_name="Pierre", last_name="Permanent", email="employed@gmail.com",
            phone="0648569745", password="mjefo4ars14-", hightest_level="3")

        cls.user_not_employed = CustomUser.objects.create(
            first_name="Pierre", last_name="Not_permanent", email="notemployed@gmail.com",
            phone="0648569745", password="kjefo4ars15-",  hightest_level="3",
            permanent_contract=False)

        cls.user_multi_qualifications = CustomUser.objects.create(
            first_name="Jarod", last_name="Cameleon", email="jc@gmail.com",
            phone="0648569745", password="65hv1j61uny", hightest_level="4")
        cls.membership_multi_hr = Membership.objects.create(
            user=cls.user_multi_qualifications, status=cls.status_hr) # level 4
        cls.membership_multi_commercial = Membership.objects.create(
            user=cls.user_multi_qualifications, status=cls.status_commercial) # level 4
        cls.membership_multi_electrotechnician = Membership.objects.create(
            user=cls.user_multi_qualifications, status=cls.status_electrotechnician) # level 3
        cls.membership_multi_apprentice = Membership.objects.create(
            user=cls.user_multi_qualifications, status=cls.status_apprentice) # level 2
        cls.membership_multi_client = Membership.objects.create(
            user=cls.user_multi_qualifications, status=cls.status_client) # level 1

        ######################## We create all variables ######################
        ######################## We create all variables ######################
        ######################## We create all variables ######################

        cls.url_entities_list = reverse_lazy('entities-list')
        cls.url_entities_detail = 'entities-detail'

        cls.url_clients_list = reverse_lazy('clients-list')
        cls.url_clients_detail = 'clients-detail'

        cls.url_installations_list = reverse_lazy('installations-list')
        cls.url_installations_detail = 'installations-detail'

        cls.con_user = APIClient()
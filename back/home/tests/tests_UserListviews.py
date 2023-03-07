import json

from .tests_datas import DatasAPITestCase
from ..serializers import CreateUserSerializer
from ..models import User


class TestUserListViews(DatasAPITestCase):
    """ Test of all UserList views. """


    def test_IsAuthenticated(self):
        """ We test the Authentication. """

        # When user is not authenticated
        response = self.con_user.get(self.url_users_list)
        self.assertEqual(response.status_code, 403)

        # When user is authenticated
        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.get(self.url_users_list)
        self.assertEqual(response.status_code, 200)


    def test_IsActive(self):
        """ We test the access with an active user and none active one. """

        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(self.url_users_list)
        self.assertEqual(response.status_code, 200)

        self.con_user.force_authenticate(self.user_not_active)
        response = self.con_user.get(self.url_users_list)
        self.assertEqual(response.status_code, 403)


    def test_IsNotClient(self):
        """ We test the access with a none client user and a client one. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.get(self.url_users_list)
        self.assertEqual(response.status_code, 200)

        self.con_user.force_authenticate(self.user_client)
        response = self.con_user.get(self.url_users_list)
        self.assertEqual(response.status_code, 403)


    def test_GetLightUserSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: LightUserSerializer. """

        self.con_user.force_authenticate(self.user_electrotechnician)
        response = self.con_user.get(self.url_users_list)

        self.assertEqual(response.status_code, 200)

        expected = [
            {
                'id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone': user.phone,
            } for user in [
                self.user_boss, self.user_accountant, self.user_hr, self.user_commercial,
                self.user_repair_operator, self.user_receptionist, self.user_stock_operator,
                self.user_electrotechnician, self.user_repairman, self.user_coppersmith,
                self.user_locksmith, self.user_mason, self.user_deliveryman, self.user_installer,
                self.user_maintenance_agent, self.user_client, self.user_supplier,
                self.user_active, self.user_employed, self.user_not_employed
            ]
        ]

        self.assertEqual(response.json(), expected)


    def test_GetHeavyUserSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: HeavyUserSerializer. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(self.url_users_list)

        self.assertEqual(response.status_code, 200)

        expected = [
            {
                'id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                "email": user.email,
                "phone": user.phone,
                "days_off": user.days_off,
                "days_off_cumul": user.days_off_cumul,
                "permanent_contract": user.permanent_contract,
            } for user in [
                self.user_boss, self.user_accountant, self.user_hr, self.user_commercial,
                self.user_repair_operator, self.user_receptionist, self.user_stock_operator,
                self.user_electrotechnician, self.user_repairman, self.user_coppersmith,
                self.user_locksmith, self.user_mason, self.user_deliveryman, self.user_installer,
                self.user_maintenance_agent, self.user_client, self.user_supplier,
                self.user_active, self.user_employed, self.user_not_employed
            ]
        ]

        self.assertEqual(response.json(), expected)


    def test_PostUserWithSuperuser(self):
        """ Test of method post with a superuser. """

        self.con_user.force_authenticate(self.superuser)

        datas = {
            'first_name': "James",
            'last_name': "Hetfield",
            'email': "metallica@gmail.com",
            'phone': "0646865234",
            'password': "masterofpuppets7745+",
        }

        nb_users = User.objects.count()

        response = self.con_user.post(self.url_users_list, data=datas, format='json')

        self.assertEqual(response.status_code, 201)

        self.assertEqual(User.objects.count(), nb_users + 1)

        new_user = User.objects.get(email="metallica@gmail.com")
        self.assertEqual(new_user.username, "metallica@gmail.com")


    def test_PostUserWithBossUser(self):
        """ Test of method post with a boss user. """

        self.con_user.force_authenticate(self.user_boss)

        datas = {
            'first_name': "Dimebag",
            'last_name': "Darell",
            'email': "pantera@gmail.com",
            'phone': "0646865234",
            'password': "vulgardisplay7745+",
        }

        nb_users = User.objects.count()

        response = self.con_user.post(self.url_users_list, data=datas, format='json')

        self.assertEqual(response.status_code, 201)

        self.assertEqual(User.objects.count(), nb_users + 1)

        new_user = User.objects.get(email="pantera@gmail.com")
        self.assertEqual(new_user.username, "pantera@gmail.com")


    def test_PostUserWithAccountanttUser(self):
        """ We make sure that a different user form superuser or boss cannot
        create a user. """

        self.con_user.force_authenticate(self.user_accountant)

        datas = {
            'first_name': "Dimebag",
            'last_name': "Darell",
            'email': "pantera@gmail.com",
            'phone': "0646865234",
            'password': "vulgardisplay7745+",
        }

        response = self.con_user.post(self.url_users_list, data=datas)

        self.assertEqual(response.status_code, 400)


    # def test_PostUserWithWrongDatas(self):

    #     self.con_user.force_authenticate(self.user_boss)

    #     response = self.con_user.post(self.url_users_lis, data="")

    #     self.assertEqual(response.status_code, 400)

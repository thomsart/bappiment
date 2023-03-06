from .tests_datas import HomeAPITestCase
from .serializers import (
    LightUserSerializer, HeavyUserSerializer, CreateUserSerializer,
    StatusSerializer, MembershipSerializer,
)


########## UserListViews ######################################################
########## UserListViews ######################################################
########## UserListViews ######################################################


class TestUserListViews(HomeAPITestCase):
    """
    Tests for light users list views:
    test code 200
    test reponse
    test acces refusé si non connecté
    test acces refusé si pas actif
    test acces refusé si client

    """


    def test_IsAuthenticated(self):
        """ We test the Authentication. """

        # When user is not authenticated
        reponse = self.con_user.get(self.url_user_list)
        self.assertEqual(reponse.status_code, 403)

        # When user is authenticated
        self.con_user.force_authenticate(self.boss)
        reponse = self.con_user.get(self.url_user_list)
        self.assertEqual(reponse.status_code, 200)


    def test_IsActive(self):

        self.con_user.force_authenticate(self.user_not_active)
        reponse = self.con_user.get(self.url_user_list)

        self.assertEqual(reponse.status_code, 400)


    def test_IsPermanentEmployee(self):

        self.con_user.force_authenticate(self.user_not_active)
        reponse = self.con_user.get(self.url_user_list)

        self.assertEqual(reponse.status_code, 403)


    def test_IsNotClient(self):

        self.con_user.force_authenticate(self.client)
        reponse = self.con_user.get(self.url_user_list)

        self.assertEqual(reponse.status_code, 400)


    def test_IsActionAllowed(self):

        # tester toutes les methode en fonction des users
        # tester le post quand il marche et quand il marche pas
        self.con_user.force_authenticate(self.user_not_active)
        reponse = self.con_user.get(self.url_user_list)

        self.assertEqual(reponse.status_code, 200)


    def test_LightUserSerializer(self):
        ...


    def test_HeavyUserSerializer(self):
        """ 
        """

        self.con_user.force_authenticate(self.boss)
        reponse = self.con_user.get(self.url_user_list)

        self.assertEqual(reponse.status_code, 200)

        expected = [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone': user.phone,
            } for user in [
                self.boss, self.accountant, self.hr, self.commercial,
                self.repair_operator, self.receptionist, self.stock_operator,
                self.electrotechnician, self.repairman, self.coppersmith,
                self.locksmith, self.mason, self.postman, self.installer,
                self.maintenance_agent, self.client
            ]
        ]

        self.assertEqual(reponse.json(), expected)


########## UserDetailViews ####################################################
########## UserDetailViews ####################################################
########## UserDetailViews ####################################################

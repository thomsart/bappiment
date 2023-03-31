from rest_framework.reverse import reverse

from .tests_datas import DatasAPITestCase
from ..models import CustomUser


class TestUserDetailViews(DatasAPITestCase):
    """ Test of all UserList views. """


    def test_IsAuthenticated(self):
        """ We test the Authentication. """

        # When user is not authenticated
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_boss.pk}
        ))
        self.assertEqual(response.status_code, 403)

        # When user is authenticated
        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_boss.pk}
        ))
        self.assertEqual(response.status_code, 200)


    def test_IsActive(self):
        """ We test the access with an active user and a deactivate one. """

        # When user is active
        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_accountant.pk}
        ))
        self.assertEqual(response.status_code, 200)

        # When user is deactivate
        self.con_user.force_authenticate(self.user_not_active)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_accountant.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_IsNotClient(self):
        """ We test the access with a client user. """

        self.con_user.force_authenticate(self.user_client)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_electrotechnician.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_GetUserDoesNotExists(self):
        """ We test to get a user that does not exists. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': 1000}
        ))
        self.assertEqual(response.status_code, 404)


    def test_GetSuperuserUnauthorised(self):
        """ We test that acces the superuser is not allowed. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.superuser.pk}
        ))
        self.assertEqual(response.status_code, 404)


    def test_GetLightUserSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: LightCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_electrotechnician)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_boss.pk}
        ))
        self.assertEqual(response.status_code, 200)

        expected = {
                'id': self.user_boss.pk,
                'first_name': self.user_boss.first_name,
                'last_name': self.user_boss.last_name,
                'phone': self.user_boss.phone,
            }
        self.assertEqual(response.json(), expected)


    def test_GetHeavyUserSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: HeavyCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_installer.pk}
        ))
        self.assertEqual(response.status_code, 200)

        expected = {
            'id': self.user_installer.pk,
            'first_name': self.user_installer.first_name,
            'last_name': self.user_installer.last_name,
            "email": self.user_installer.email,
            "phone": self.user_installer.phone,
            "days_off": self.user_installer.days_off,
            "days_off_cumul": self.user_installer.days_off_cumul,
            "permanent_contract": self.user_installer.permanent_contract,
        }

        self.assertEqual(response.json(), expected)



    def test_updateUser(self):
        ...



    def test_DeleteUserByBoss(self):
        """ We test to delete a user with the boss. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_installer.pk}
        ))
        self.assertEqual(response.status_code, 204)


    def test_DeleteUserByAccountant(self):
        """ We test to delete a user with an accountant. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_installer.pk}
        ))
        self.assertEqual(response.status_code, 401)


    def test_DeleteUserByElectrotechnician(self):
        """ We test to delete a user with an electrotechnician. """

        self.con_user.force_authenticate(self.user_electrotechnician)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_installer.pk}
        ))
        self.assertEqual(response.status_code, 401)


    def test_DeleteUserByApprentice(self):
        """ We test to delete a user with an apprentice. """

        self.con_user.force_authenticate(self.user_apprentice)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_client.pk}
        ))
        self.assertEqual(response.status_code, 401)


    def test_DeleteUserByClient(self):
        """ We test to delete a user with a client. """

        self.con_user.force_authenticate(self.user_client)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_apprentice.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_DeleteUserDoesNotExists(self):
        """ We test to delete a user which does not exists. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': 1000}
        ))
        self.assertEqual(response.status_code, 404)
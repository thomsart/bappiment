from rest_framework.reverse import reverse

from .datas import HomeDatasAPITestCase



class TestUserDetailViews(HomeDatasAPITestCase):
    """ Test of all Home application's views. """


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
        """ We test that access to the superuser is not allowed. """

        self.con_user.force_authenticate(self.user_apprentice)
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

        expected_datas = {
            'id': self.user_boss.pk,
            'first_name': self.user_boss.first_name,
            'last_name': self.user_boss.last_name,
            'phone': self.user_boss.phone,
        }

        self.assertEqual(response.json(), expected_datas)


    def test_GetHeavyUserSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: HeavyCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.user_installer.pk}
        ))
        self.assertEqual(response.status_code, 200)

        expected_datas = {
            'id': self.user_installer.pk,
            'first_name': self.user_installer.first_name,
            'last_name': self.user_installer.last_name,
            "email": self.user_installer.email,
            "phone": self.user_installer.phone,
            "days_off": self.user_installer.days_off,
            "days_off_cumul": self.user_installer.days_off_cumul,
            "permanent_contract": self.user_installer.permanent_contract,
        }

        self.assertEqual(response.json(), expected_datas)


    def test_updateUserWithBossUser(self):
        """ We test here that the boss can update a user. """

        self.con_user.force_authenticate(self.user_boss)

        self.assertEqual(self.user_not_employed.permanent_contract, False)

        datas = {
            'first_name': self.user_not_employed.first_name,
            'last_name': self.user_not_employed.last_name,
            'email': self.user_not_employed.email,
            'phone': self.user_not_employed.phone,
            'permanent_contract': "true"
        }

        response = self.con_user.put(
            reverse(self.url_users_detail, kwargs={'pk': self.user_not_employed.pk}),
            data=datas
        )

        expected_datas = {
            'id': self.user_not_employed.pk,
            'first_name': self.user_not_employed.first_name,
            'last_name': self.user_not_employed.last_name,
            'email': self.user_not_employed.email,
            'phone': self.user_not_employed.phone,
            'days_off': self.user_not_employed.days_off,
            'days_off_cumul': self.user_not_employed.days_off_cumul,
            'permanent_contract': True
        }

        self.assertEqual(response.json(), expected_datas)


    def test_updateUserWithForbiddenUser(self):
        """ We test here that an accountant cannot update a user. """

        self.con_user.force_authenticate(self.user_accountant)

        self.assertEqual(self.user_not_employed.permanent_contract, False)

        datas = {
            'first_name': self.user_not_employed.first_name,
            'last_name': self.user_not_employed.last_name,
            'email': self.user_not_employed.email,
            'phone': self.user_not_employed.phone,
            'permanent_contract': "true"
        }

        response = self.con_user.put(
            reverse(self.url_users_detail, kwargs={'pk': self.user_not_employed.pk}),
            data=datas
        )

        self.assertEqual(response.status_code, 403)


    def test_updateUserWithWrongDatas(self):
        """ We test here the updating with wrong datas. """

        self.con_user.force_authenticate(self.user_boss)

        self.assertEqual(self.user_not_employed.permanent_contract, False)

        datas = {
            'first_name': self.user_not_employed.first_name,
            'last_name': self.user_not_employed.last_name,
            'email': self.user_not_employed.email,
            'phone': self.user_not_employed.phone,
            'permanent_contract': self.user_not_employed.phone
        }

        response = self.con_user.put(
            reverse(self.url_users_detail, kwargs={'pk': self.user_not_employed.pk}),
            data=datas
        )

        self.assertEqual(response.status_code, 400)


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
        self.assertEqual(response.status_code, 403)


    def test_DeleteUserByElectrotechnician(self):
        """ We test to delete a user with an electrotechnician. """

        self.con_user.force_authenticate(self.user_electrotechnician)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_installer.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_DeleteUserByApprentice(self):
        """ We test to delete a user with an apprentice. """

        self.con_user.force_authenticate(self.user_apprentice)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_client.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_DeleteUserByClient(self):
        """ We test to delete a user with a client. """

        self.con_user.force_authenticate(self.user_client)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.user_apprentice.pk}))
        self.assertEqual(response.status_code, 403)


    def test_DeleteUserDoesNotExists(self):
        """ We test to delete a user which does not exists. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': 1000}
        ))
        self.assertEqual(response.status_code, 404)
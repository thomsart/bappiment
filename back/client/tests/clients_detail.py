import datetime

from rest_framework.reverse import reverse

from .datas import ClientDatasAPITestCase



class TestClientDetailViews(ClientDatasAPITestCase):
    """ Test of ClientDetail views. """


    def test_IsActive(self):
        """ We test the access with an active user and a deactivate one. """

        # When user is active
        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': self.client_one.pk}
        ))
        self.assertEqual(response.status_code, 200)

        # When user is deactivate
        self.con_user.force_authenticate(self.user_not_active)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': self.client_one.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_IsNotClient(self):
        """ We test the access with a client user. """

        self.con_user.force_authenticate(self.user_client)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': self.client_one.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_GetCanceledClient(self):
        """ We test to get an canceled client. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': self.client_canceled.pk}
        ))
        self.assertEqual(response.status_code, 404)


    def test_GetClientDoesNotExists(self):
        """ We test to get a user that does not exists. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': 1000}
        ))
        self.assertEqual(response.status_code, 404)


    def test_GetLightClientSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: LightCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_electrotechnician)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': self.client_one.pk}
        ))
        self.assertEqual(response.status_code, 200)

        expected_datas = {
            'legal_entity': {'name': self.legal_entity_family.name},
            'name': self.client_one.name,
            'nb_street': self.client_one.nb_street,
            'street': self.client_one.street,
            'zip_code': self.client_one.zip_code,
            'city': self.client_one.city,
            'country': self.client_one.country,
            'contact': self.user_client_one.pk
        }

        self.assertEqual(response.json(), expected_datas)


    def test_GetHeavyClientSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: HeavyCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(reverse(
            self.url_clients_detail, kwargs={'pk': self.client_two.pk}
        ))
        self.assertEqual(response.status_code, 200)

        expected_datas = {
            'legal_entity': {'name': self.legal_entity_syndic.name},
            'name': self.client_two.name,
            'siren': self.client_two.siren,
            'siret': self.client_two.siret,
            'nb_street': self.client_two.nb_street,
            'street': self.client_two.street,
            'zip_code': self.client_two.zip_code,
            'city': self.client_two.city,
            'country': self.client_two.country,
            'date': str(self.client_two.date),
            'contact': self.user_client_two.pk
        }

        self.assertEqual(response.json(), expected_datas)


    def test_updateClientWithBossUser(self):
        """ We test here that the boss can update a user. """

        self.con_user.force_authenticate(self.user_boss)

        self.assertEqual(self.client_three.is_still_client, True)

        datas = {
            'legal_entity': {'name': self.legal_entity_company.name},
            'name': self.client_three.name,
            'siren': self.client_three.siren,
            'siret': self.client_three.siret,
            'nb_street': self.client_three.nb_street,
            'street': self.client_three.street,
            'zip_code': self.client_three.zip_code,
            'city': self.client_three.city,
            'country': self.client_three.country,
            'date': str(self.client_three.date),
            'contact': self.user_client_three.pk
        }

        response = self.con_user.put(
            reverse(self.url_clients_detail, kwargs={'pk': self.client_three.pk}),
            data=datas
        )

        expected_datas = {
            'legal_entity': {'name': self.legal_entity_company.name},
            'name': self.client_three.name,
            'siren': self.client_three.siren,
            'siret': self.client_three.siret,
            'nb_street': self.client_three.nb_street,
            'street': self.client_three.street,
            'zip_code': self.client_three.zip_code,
            'city': self.client_three.city,
            'country': self.client_three.country,
            'date': str(self.client_three.date),
            'contact': self.user_client_three.pk
        }

        self.assertEqual(response.json(), expected_datas)


    # def test_updateClientWithForbiddenUser(self):
    #     """ We test here that an accountant cannot update a user. """

    #     self.con_user.force_authenticate(self.user_accountant)

    #     self.assertEqual(self.user_not_employed.permanent_contract, False)

    #     datas = {
    #         'first_name': self.user_not_employed.first_name,
    #         'last_name': self.user_not_employed.last_name,
    #         'email': self.user_not_employed.email,
    #         'phone': self.user_not_employed.phone,
    #         'permanent_contract': "true"
    #     }

    #     response = self.con_user.put(
    #         reverse(self.url_clients_detail, kwargs={'pk': self.user_not_employed.pk}),
    #         data=datas
    #     )

    #     self.assertEqual(response.status_code, 403)


    # def test_updateClientWithWrongDatas(self):
    #     """ We test here the updating with wrong datas. """

    #     self.con_user.force_authenticate(self.user_boss)

    #     self.assertEqual(self.user_not_employed.permanent_contract, False)

    #     datas = {
    #         'first_name': self.user_not_employed.first_name,
    #         'last_name': self.user_not_employed.last_name,
    #         'email': self.user_not_employed.email,
    #         'phone': self.user_not_employed.phone,
    #         'permanent_contract': self.user_not_employed.phone
    #     }

    #     response = self.con_user.put(
    #         reverse(self.url_clients_detail, kwargs={'pk': self.user_not_employed.pk}),
    #         data=datas
    #     )

    #     self.assertEqual(response.status_code, 400)


    # def test_DeleteClientByBoss(self):
    #     """ We test to delete a user with the boss. """

    #     self.con_user.force_authenticate(self.user_boss)
    #     response = self.con_user.delete(reverse(
    #         self.url_clients_detail, kwargs={'pk': self.user_installer.pk}
    #     ))
    #     self.assertEqual(response.status_code, 204)


    # def test_DeleteClientByAccountant(self):
    #     """ We test to delete a user with an accountant. """

    #     self.con_user.force_authenticate(self.user_accountant)
    #     response = self.con_user.delete(reverse(
    #         self.url_clients_detail, kwargs={'pk': self.user_installer.pk}
    #     ))
    #     self.assertEqual(response.status_code, 403)


    # def test_DeleteClientByElectrotechnician(self):
    #     """ We test to delete a user with an electrotechnician. """

    #     self.con_user.force_authenticate(self.user_electrotechnician)
    #     response = self.con_user.delete(reverse(
    #         self.url_clients_detail, kwargs={'pk': self.user_installer.pk}
    #     ))
    #     self.assertEqual(response.status_code, 403)


    # def test_DeleteClientByApprentice(self):
    #     """ We test to delete a user with an apprentice. """

    #     self.con_user.force_authenticate(self.user_apprentice)
    #     response = self.con_user.delete(reverse(
    #         self.url_clients_detail, kwargs={'pk': self.user_client.pk}
    #     ))
    #     self.assertEqual(response.status_code, 403)


    # def test_DeleteClientByClient(self):
    #     """ We test to delete a user with a client. """

    #     self.con_user.force_authenticate(self.user_client)
    #     response = self.con_user.delete(reverse(
    #         self.url_clients_detail, kwargs={'pk': self.user_apprentice.pk}))
    #     self.assertEqual(response.status_code, 403)


    # def test_DeleteClientDoesNotExists(self):
    #     """ We test to delete a user which does not exists. """

    #     self.con_user.force_authenticate(self.user_boss)
    #     response = self.con_user.delete(reverse(
    #         self.url_clients_detail, kwargs={'pk': 1000}
    #     ))
    #     self.assertEqual(response.status_code, 404)
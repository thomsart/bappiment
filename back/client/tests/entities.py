from rest_framework.reverse import reverse

from .datas import ClientDatasAPITestCase



class TestEntitiesDetailViews(ClientDatasAPITestCase):
    """ Test of all Client application's views. """


    def test_IsActive(self):
        """ We test the access with an active user and non-active one. """

        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(self.url_entities_list)
        self.assertEqual(response.status_code, 200)

        self.con_user.force_authenticate(self.user_not_active)
        response = self.con_user.get(self.url_entities_list)
        self.assertEqual(response.status_code, 403)


    def test_IsNotClient(self):
        """ We test the access with a client user. """

        self.con_user.force_authenticate(self.user_client)

        list_response = self.con_user.get(self.url_entities_list)
        self.assertEqual(list_response.status_code, 403)


    def test_GetOneEntity(self):
        """ We test to get a specific status with an accountant user. """

        self.con_user.force_authenticate(self.user_accountant)

        expected_data = {
            "id": self.legal_entity_family.pk,
            "name": self.legal_entity_family.name
        }

        response = self.con_user.get(reverse(
            self.url_entities_detail, kwargs={'pk': self.legal_entity_family.pk}
        ))
        self.assertEqual(response.json(), expected_data)


    def test_GetAllEntities(self):
        """ We test to get all status with an accountant user. """

        self.con_user.force_authenticate(self.user_mason)

        expected_data = [{
            "id": entity.pk,
            "name": entity.name
        } for entity in [
            self.legal_entity_family, self.legal_entity_syndic,
            self.legal_entity_company, self.legal_entity_association,
            self.legal_entity_municipality
        ]]

        response = self.con_user.get(self.url_entities_list)

        self.assertEqual(response.json(), expected_data)
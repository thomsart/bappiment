from rest_framework.reverse import reverse

from .datas import HomeDatasAPITestCase



class TestStatusDetailViews(HomeDatasAPITestCase):
    """ Test of all Home application's views. """


    def test_IsActive(self):
        """ We test the access with an active user and non-active one. """

        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(self.url_status_list)
        self.assertEqual(response.status_code, 200)

        self.con_user.force_authenticate(self.user_not_active)
        response = self.con_user.get(self.url_status_list)
        self.assertEqual(response.status_code, 403)


    def test_IsNotClient(self):
        """ We test the access with a client user. """

        self.con_user.force_authenticate(self.user_client)

        list_response = self.con_user.get(self.url_status_list)
        self.assertEqual(list_response.status_code, 403)


    def test_GetOneStatus(self):
        """ We test to get a specific status with an accountant user. """

        self.con_user.force_authenticate(self.user_accountant)

        expected_data = {
            "id": self.status_hr.pk,
            "name": self.status_hr.name,
            "level": self.status_hr.level
        }

        response = self.con_user.get(reverse(
            self.url_status_detail, kwargs={'pk': self.status_hr.pk}
        ))
        self.assertEqual(response.json(), expected_data)


    def test_GetAllStatus(self):
        """ We test to get all status with an accountant user. """

        self.user_mason.refresh_from_db()
        self.con_user.force_authenticate(self.user_mason)

        expected_data = [{
            "id": status.pk,
            "name": status.name,
            "level": status.level
        } for status in [
            self.status_boss, self.status_accountant, self.status_hr,
            self.status_commercial, self.status_repair_operator,
            self.status_receptionist, self.status_stock_operator,
            self.status_electrotechnician, self.status_repairman,
            self.status_coppersmith, self.status_locksmith,
            self.status_mason, self.status_deliveryman,
            self.status_cleaner, self.status_installer,
            self.status_maintenance_agent, self.status_apprentice,
            self.status_client, self.status_supplier
        ]]

        response = self.con_user.get(self.url_status_list)

        self.assertEqual(response.json(), expected_data)
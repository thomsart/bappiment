from rest_framework.reverse import reverse

from .tests_datas import DatasAPITestCase
from ..models import Membership


class TestMembershipsListViews(DatasAPITestCase):
    """ Test of all MembershipsList views. """


    def test_IsAuthenticated(self):
        """ We test the Authentication. """

        # When user is not authenticated
        response = self.con_user.get(self.url_memberships_list)

        self.assertEqual(response.status_code, 403)

        # When user is authenticated
        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(self.url_memberships_list)

        self.assertEqual(response.status_code, 200)


    def test_IsActive(self):
        """ We test the access with an active user and a deactivate one. """

        # When user is active
        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(self.url_memberships_list)

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
        response = self.con_user.get(self.url_memberships_list)

        self.assertEqual(response.status_code, 403)


    def test_GetAllLighMembershipsSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: LightCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_electrotechnician)
        response = self.con_user.get(self.url_memberships_list)

        self.assertEqual(response.status_code, 200)

        expected_datas = [
            {
                "id": membership.pk,
                "status": {
                    "id": membership.status.pk,
                    "name": membership.status.name,
                    "level": membership.status.level
                },
                "user": {
                    "id": membership.user.pk,
                    "first_name": membership.user.first_name,
                    "last_name": membership.user.last_name,
                    "phone": membership.user.phone
                },
                "date": str(membership.date)
            } for membership in [
                self.membership_boss, self.membership_accountant, self.membership_hr,
                self.membership_commercial, self.membership_repair_operator,
                self.membership_receptionist, self.membership_stock_operator,
                self.membership_electrotechnician, self.membership_repairman,
                self.membership_coppersmith, self.membership_locksmith,
                self.membership_mason, self.membership_deliveryman,
                self.membership_installer, self.membership_maintenance_agent,
                self.membership_apprentice, self.membership_client
            ]
        ]

        self.assertEqual(response.json(), expected_datas)


    def test_GetAllHeavyMembershipsSerializer(self):
        """ We test here that the returned response match with the serializer
        we are supposed to received: HeavyCustomUserSerializer. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(self.url_memberships_list)

        self.assertEqual(response.status_code, 200)

        expected_datas = [
            {
                "id": membership.pk,
                "status": {
                    "id": membership.status.pk,
                    "name": membership.status.name,
                    "level": membership.status.level
                },
                "user": {
                    "id": membership.user.pk,
                    "first_name": membership.user.first_name,
                    "last_name": membership.user.last_name,
                    "email": membership.user.email,
                    "phone": membership.user.phone,
                    "days_off": membership.user.days_off,
                    "days_off_cumul": membership.user.days_off_cumul,
                    "permanent_contract": membership.user.permanent_contract
                },
                "date": str(membership.date)
            } for membership in [
                self.membership_boss, self.membership_accountant, self.membership_hr,
                self.membership_commercial, self.membership_repair_operator,
                self.membership_receptionist, self.membership_stock_operator,
                self.membership_electrotechnician, self.membership_repairman,
                self.membership_coppersmith, self.membership_locksmith,
                self.membership_mason, self.membership_deliveryman,
                self.membership_installer, self.membership_maintenance_agent,
                self.membership_apprentice, self.membership_client
            ]
        ]

        self.assertEqual(response.json(), expected_datas)
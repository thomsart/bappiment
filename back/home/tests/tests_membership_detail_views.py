from rest_framework.reverse import reverse

from .tests_datas import DatasAPITestCase
from ..models import CustomUser


class TestMembershipDetailViews(DatasAPITestCase):
    """ Test of all UserList views. """


    def test_IsAuthenticated(self):
        """ We test the Authentication. """

        # When user is not authenticated
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.membership_accountant.pk}
        ))
        self.assertEqual(response.status_code, 403)

        # When user is authenticated
        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.membership_accountant.pk}
        ))
        self.assertEqual(response.status_code, 200)


    def test_IsActive(self):
        """ We test the access with an active user and a deactivate one. """

        # When user is active
        self.con_user.force_authenticate(self.user_active)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.membership_accountant.pk}
        ))
        self.assertEqual(response.status_code, 200)

        # When user is deactivate
        self.con_user.force_authenticate(self.user_not_active)
        response = self.con_user.get(reverse(
            self.url_users_detail, kwargs={'pk': self.membership_accountant.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_DeleteMembershipWithBossUser(self):
        """ We test to delete a user with the boss. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.membership_electrotechnician.pk}
        ))
        self.assertEqual(response.status_code, 204)


    def test_DeleteMembershipWithAccountantUser(self):
        """ We test to delete a user with the boss. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': self.membership_electrotechnician.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_DeleteMembershipDoesNotExists(self):
        """ We test to delete a user which does not exists. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_users_detail, kwargs={'pk': 1000}
        ))
        self.assertEqual(response.status_code, 404)


    def test_DeleteMembershipWhenUserHasJustOneStatus(self):
        """  """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_memberships_detail, kwargs={'pk': self.membership_hr.pk}
        ))
        self.assertEqual(response.status_code, 403)


    def test_DeleteMembershipAndCheckTheHightestlevel(self):
        """  """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_memberships_detail, kwargs={'pk': self.user_multi_qualifications_hr.pk}
        ))
        print(type(self.user_multi_qualifications.hightest_level))

        self.assertEqual(self.user_multi_qualifications.hightest_level, '4')
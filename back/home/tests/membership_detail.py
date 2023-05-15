from rest_framework.reverse import reverse

from .datas import HomeDatasAPITestCase


class TestMembershipDetailViews(HomeDatasAPITestCase):
    """ Test of all UserList views. """


    def test_DeleteMembershipWithAccountantUser(self):
        """ We test to delete a user with the boss. """

        self.con_user.force_authenticate(self.user_accountant)
        response = self.con_user.delete(reverse(
            self.url_memberships_detail, kwargs={'pk': self.membership_electrotechnician.pk}))
        self.assertEqual(response.status_code, 403)


    def test_DeleteMembershipWithBossUser(self):
        """ We test to delete a user with the boss. """

        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_memberships_detail, kwargs={'pk': self.membership_cleaner.pk}))
        self.assertEqual(response.status_code, 204)


    def test_DeleteMembershipDoesNotExists(self):
        """ We test to delete a user which does not exists. """

        self.user_boss.refresh_from_db()
        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_memberships_detail, kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, 404)


    def test_DeleteMembershipWhenUserHasJustOneStatus(self):
        """  """

        self.user_boss.refresh_from_db()
        self.con_user.force_authenticate(self.user_boss)
        response = self.con_user.delete(reverse(
            self.url_memberships_detail, kwargs={'pk': self.membership_hr.pk}))
        self.assertEqual(response.status_code, 403)


    def test_DeleteMembershipsAndCheckTheHightestlevel(self):
        """  """

        self.user_boss.refresh_from_db()
        self.con_user.force_authenticate(self.user_boss)
        self.con_user.delete(reverse(
            self.url_memberships_detail,
            kwargs={'pk': self.membership_multi_hr.pk}))
        self.user_multi_qualifications.refresh_from_db()
        self.assertEqual(self.user_multi_qualifications.hightest_level, '4')

        self.con_user.delete(reverse(
            self.url_memberships_detail,
            kwargs={'pk': self.membership_multi_apprentice.pk}))
        self.user_multi_qualifications.refresh_from_db()
        self.assertEqual(self.user_multi_qualifications.hightest_level, '4')

        self.con_user.delete(reverse(
            self.url_memberships_detail,
            kwargs={'pk': self.membership_multi_commercial.pk}))
        self.user_multi_qualifications.refresh_from_db()
        self.assertEqual(self.user_multi_qualifications.hightest_level, '3')

        self.con_user.delete(reverse(
            self.url_memberships_detail,
            kwargs={'pk': self.membership_multi_electrotechnician.pk}))
        self.user_multi_qualifications.refresh_from_db()
        self.assertEqual(self.user_multi_qualifications.hightest_level, '1')

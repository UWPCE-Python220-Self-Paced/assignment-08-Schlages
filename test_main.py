"""Test python file to test all functions and methods for users and user_status"""
from unittest import TestCase
import main
from playhouse.dataset import DataSet


dataset = DataSet('sqlite:///socialnetwork2.db')

users_table = dataset['userstable']
users_table.insert(USER_ID='scout19')
users_table.create_index(['USER_ID'], unique=True)
users_table.delete(USER_ID='scout19')

status_table = dataset['userstatustable']
status_table.insert(STATUS_ID='bschlagel91_00001')
status_table.create_index(['STATUS_ID'], unique=True)
status_table.delete(STATUS_ID='bschlagel91_00001')

class UserTests(TestCase):
    """Class to test all functions and methods"""
    def test_add_user(self):
        """Check to for duplicates"""

        main.delete_user('anni92', users_table, status_table)
        # true, because anni92 is a new user_id
        test = main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        expected = True

        self.assertEqual(test, expected)

        test_add = main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        expected = False
        self.assertEqual(test_add, expected)
        main.delete_user('anni92', users_table, status_table)
    def test_update_user(self):
        """Run a Testcase to check if we are able to save new instances to file"""

        main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        user = main.update_user('anni92', 'newnew', 'neweve', 'newmiles', users_table)
        expected_result = True
        self.assertEqual(user, expected_result)

        # False, because scout19 is a new user_id
        update_test = main.update_user('scout19', '', '', '', users_table)
        expected_update = False
        self.assertEqual(update_test, expected_update)
    def test_delete_user(self):
        """Check to see if scout19 exists"""

        main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        # true because anni92 exists
        delete_test = main.delete_user('anni92', users_table, status_table)
        expected = True
        self.assertEqual(delete_test, expected)

        # false because scout19 does not exists
        delete_test = main.delete_user('scout19', users_table, status_table)
        expected = False
        self.assertEqual(delete_test, expected)
    def test_search_user(self):
        """Check to see if anni92 exists"""

        main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        # user does not exist, so returns none
        search_test = main.search_user('scout19', users_table)
        expected = None
        self.assertEqual(search_test, expected)

        # True, because this exists in dataset
        test = main.search_user('Brittaney.Gentry86', users_table)
        expected = {'id': 1, 'USER_ID': 'Brittaney.Gentry86', 'NAME': 'Brittaney', 'LASTNAME': 'Gentry',
                    'EMAIL': 'Brittaney.Gentry86@goodmail.com'}

        self.assertEqual(test, expected)


    def testadd_status(self):
        """Run a Testcase to check if we are able to save new instances to file"""

        main.delete_status('anni92_0001', status_table)
        test_add = main.add_status('anni92_0001', 'anni92',
                                   'Code is finally compiling', status_table, users_table)
        expected = True
        self.assertEqual(test_add, expected)

         # true, because anni92 does not exist
        test_add = main.add_status('anni92_0001', '', '', status_table, users_table)
        expected = False
        self.assertEqual(test_add, expected)


    def test_update_status(self):
        """Check to see if status update exists"""

        main.delete_status('anni92_0001', status_table)
        main.add_status('anni92_0001', 'anni92','Code is finally compiling',
                        status_table, users_table)

        # false because status id does not exist
        test_update = main.update_status('Anni92_00001', '','', status_table)
        expectedstatus = False
        self.assertEqual(test_update, expectedstatus)

        # True because anni92_0001 exists
        update_test = main.update_status('anni92_0001', 'anni92',
                                         'sharp flock peel astonishing loaf',
                                         status_table)
        expected_update = True
        self.assertEqual(update_test, expected_update)

    def test_delete_status(self):
        """Run a unit test to check if scout19 status id exists"""

        main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        main.add_status('anni92_0001', 'anni92',
                        'Code is finally compiling', status_table, users_table)

        # true because anni92 exists
        delete_test = main.delete_status('anni92_0001', status_table)
        expected = True
        self.assertEqual(delete_test, expected)

        # false because bschlagel91 does not exists
        delete_test = main.delete_status('scout18', status_table)
        expected = False
        self.assertEqual(delete_test, expected)


    def test_search_status(self):
        """Run unit test to check if scout19_00001 status id exists"""
        main.add_user('anni92', 'anni92.@gmail.com', 'Annika', 'Skaugrud', users_table)
        main.add_status('anni92_0001', 'anni92', 'Code is finally compiling',
                        status_table, users_table)

        # True, because this exists in dataset
        test = main.search_status('Isabel.Avivah34_27', status_table)
        expected = {'id': 1, 'STATUS_ID': 'Isabel.Avivah34_27', 'USER_ID': 'Isabel.Avivah34',
                    'STATUS_TEXT': 'thinkable existence hug aback sky'}

        self.assertEqual(test, expected)

        # user does not exist, so returns none
        search_test = main.search_status('anni92_0000122', status_table)
        expected = None
        self.assertEqual(search_test, expected)


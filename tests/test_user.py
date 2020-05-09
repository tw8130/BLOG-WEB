import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    Test to test behaviour of user model class
    '''

    def setUp(self):
        '''
        Method that creates instance of user class and pass paswword property
        '''
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        '''
        Acsertains if password is being hashed  and if pass_secure contains a value
        '''
        self.assertTrue(self.new_user.password_hash is not None)

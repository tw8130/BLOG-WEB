import unittest
from app.models import  Blog
from datetime import datetime
class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the blog post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Blog(1,
                            1,
                             'Python Must Be Crazy',
                             '2020-04-05 08:26:19.580874',
                             'Cryptography',
                             'Great subject')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Blog))
        
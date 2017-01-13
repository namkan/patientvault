from django.test import TestCase
from registration.models import *

class PvUserTestCase(TestCase):
	def setUp(self):
		PvUser.objects.create(mobile_number = 9899989998,email='bikram.bharti99@gmail.com')
		PvUser.objects.create(mobile_number = 9898989898,email='namankansal32@gmail.com')

	def test_if_data_entered(self):
		'''
		PvUser which are successfully created 
		pass the test
		'''
		bikram = PvUser.objects.get(email = 'bikram.bharti99@gmail.com')
		naman = PvUser.objects.get(email = 'namankansal32@gmail.com')
		self.assertEqual(bikram.mobile_number,9899989998)
		self.assertEqual(naman.mobile_number,9898989898)
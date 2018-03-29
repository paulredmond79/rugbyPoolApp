from django.test import TestCase
import datetime

# Create your tests here.
from .models import *

def create_series(name,length_days):
	return series.objects.create(name=name,start_date=timezone.now(),end_date= timezone.now() + datetime.timedelta(days=length_days))

def create_match(opposition,match_series,kick_off_time,location):
	return match.objects.create(opposition=opposition,match_series=match_series,kick_off_time=kick_off_time,location=location)


class matchModelTests(TestCase):
	def test_name_generated_correctly(self):
		test_series = create_series('Six Nations 2018',25)
		test_match = create_match('England',test_series,timezone.now(),'Twickenham')
		self.assertEqual(test_match.name,'England @ Twickenham - Six Nations 2018')
		


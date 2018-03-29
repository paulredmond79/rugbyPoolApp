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
	def test_future_match_not_kicked_off(self):
		test_series = create_series('Six Nations 2018',25)
		future_match = create_match('England',test_series,timezone.now() + datetime.timedelta(days=1),'Twickenham')
		self.assertEqual(future_match.has_kicked_off(), False)
	def test_future_match_not_kicked_off_result_none(self):
		test_series = create_series('Six Nations 2018',25)
		future_match = create_match('England',test_series,timezone.now() + datetime.timedelta(days=1),'Twickenham')
		self.assertEqual(future_match.result, None)
	def test_past_match_has_kicked_off(self):
		test_series = create_series('Six Nations 2018',25)
		past_match = create_match('England',test_series,timezone.now() - datetime.timedelta(days=1),'Twickenham')
		self.assertEqual(past_match.has_kicked_off(), True)
	def test_past_match_has_kicked_result_not_none(self):
		test_series = create_series('Six Nations 2018',25)
		past_match = create_match('England',test_series,timezone.now() - datetime.timedelta(days=1),'Twickenham')
		self.assertNotEqual(past_match.result,None)
	def test_match_draw(self):
		test_series = create_series('Six Nations 2018',25)
		past_match = create_match('England',test_series,timezone.now() - datetime.timedelta(days=1),'Twickenham')
		past_match.opposition_score = 10
		past_match.our_score = 10
		self.assertEqual(past_match.result,'draw')
	def test_match_opposition_win(self):
		test_series = create_series('Six Nations 2018',25)
		past_match = create_match('England',test_series,timezone.now() - datetime.timedelta(days=1),'Twickenham')
		past_match.opposition_score = 15
		past_match.our_score = 10
		self.assertEqual(past_match.result,'opposition')
	def test_match_us_win(self):
		test_series = create_series('Six Nations 2018',25)
		past_match = create_match('England',test_series,timezone.now() - datetime.timedelta(days=1),'Twickenham')
		past_match.opposition_score = 10
		past_match.our_score = 15
		self.assertEqual(past_match.result,'us')

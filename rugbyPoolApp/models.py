from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import math


# Create your models here.

class baseObject(models.Model):


	create_date = models.DateTimeField('date created', default=timezone.now,editable=False)

class series(baseObject):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()


class match(baseObject):
	opposition = models.CharField(max_length=200)
	kick_off_time = models.DateTimeField()
	match_series = models.ForeignKey(series, on_delete=models.CASCADE)
	location = models.CharField(max_length=200)
	@property
	def name(self):
		return '{0} @ {1} - {2}'.format(self.opposition,self.location,self.match_series)
	def has_kicked_off(self):
		now = timezone.now()
		return self.kick_off_time <= now
	opposition_score = models.IntegerField(default=0)
	our_score = models.IntegerField(default=0)
	@property
	def result(self):
		if self.has_kicked_off():
			if self.opposition_score > self.our_score:
				return 'opposition'
			elif self.opposition_score < self.our_score:
				return 'us'
			else:
				return 'draw'
		else:
			return None
	def __str__(self):
		return self.name


class prediction(baseObject):
	"""Represents a user's score prediction for a match."""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	prediction_match = models.ForeignKey(match, on_delete=models.CASCADE)
	our_score = models.IntegerField(default=0)
	opposition_score = models.IntegerField(default=0)
	@property
	def name(self):
		return '{0} - {1}'.format(self.user,self.prediction_match.name)
	@property
	def distance(self):
		if self.prediction_match.has_kicked_off():
			return math.sqrt(math.pow(self.prediction_match.our_score - self.our_score,2) + math.pow(self.prediction_match.opposition_score - self.opposition_score,2))
		else:
			return None
	@property
	def predicted_result(self):
		if self.opposition_score > self.our_score:
			return 'opposition'
		elif self.opposition_score < self.our_score:
			return 'us'
		else:
			return 'draw'
	@property
	def correct_result(self):
		if self.prediction_match.has_kicked_off():
			return self.predicted_result == self.prediction_match.result

		else:
			return None
	def __str__(self):
		return self.name

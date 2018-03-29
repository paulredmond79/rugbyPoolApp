from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


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
		return now - datetime.timedelta(days=1) <= self.kick_off_time <= now
	opposition_score = models.IntegerField(default=0)
	our_score = models.IntegerField(default=0)
	@property
	def result(self):
		if self.has_kicked_off():
			if opposition_score > our_score:
				return 'opposition'
			elif opposition_score < our_score:
				return 'us'
			else:
				return 'draw'
		else:
			return None


class prediction(baseObject):
	"""docstring for prediction"""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	prediction_match = models.ForeignKey(match, on_delete=models.CASCADE)
	our_score = models.IntegerField(default=0)
	opposition_score = models.IntegerField(default=0)
	@property
	def name(self):
		return '{0} - {1}'.format(self.user,self.prediction_match.name)
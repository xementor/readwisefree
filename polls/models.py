import datetime
from django.db import models
from django.utils import timezone
from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=40)
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Question(models.Model): #extended Model
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') 
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	# user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.choice_text


class Vote(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
	# votes = models.IntegerField(default=0)



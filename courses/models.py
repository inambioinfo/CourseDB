from django.db import models

class Duration(models.Model):
	length_text = models.CharField(max_length=200)
	hours = models.IntegerField(default=0)
	current_cost_pence = models.IntegerField(default=0)
	
	def __str__(self):
		return self.length_text

class Course(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	duration = models.ForeignKey(Duration,on_delete=models.PROTECT)
	currently_available = models.BooleanField(default=True)
	
	def __str__(self):
		return self.title
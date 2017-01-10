from django.db import models
from django.contrib.auth.models import User

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

class CourseInstance(models.Model):
	course = models.ForeignKey(Course,on_delete=models.PROTECT)
	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField()
	site = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	spaces = models.IntegerField(default=0)
	
	def is_full(self):
		return len(self.booking_set.all()) >= self
	
	def __str__(self):
		return self.course.title+":"+str(self.start_datetime)

class Booking(models.Model):
	course_instance = models.ForeignKey(CourseInstance, on_delete=models.PROTECT)
	person = models.ForeignKey(User, on_delete=models.PROTECT)
	date_booked = models.DateTimeField()
	
	def __str__(self):
		return self.user.email+" on "+self.course_instance.course.title

class Request(models.Model):
	course = models.ForeignKey(Course, on_delete=models.PROTECT)
	person = models.ForeignKey(User, on_delete=models.PROTECT)
	date_requested = models.DateTimeField()
	
	def __str__(self):
		return self.user.email+" on "+self.course.title

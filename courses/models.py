from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
		return len(self.booking_set.all()) >= self.spaces
	
	def has_run(self):
		return self.start_datetime <= now
	
	def __str__(self):
		return self.course.title+":"+str(self.start_datetime)

class UserDetails(models.Model):
	person = models.ForeignKey(User,on_delete=models.PROTECT)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	
	def __str__(self):
		return self.first_name+" "+self.last_name

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

class LearningObjective(models.Model):
	objective_text = models.CharField(max_length=255)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.objective_text


class Feedback(models.Model):
	code = models.CharField(max_length=200, db_index=True)
	comments = models.TextField()
	course_instance = models.ForeignKey(CourseInstance, on_delete=models.CASCADE)

	def __str__(self):
		return "Feedback code="+self.code+" on "+course_instance.course.title

class FeedbackResponse(models.Model):
	value = models.IntegerField()
	feedback = models.ForeignKey(Feedback, on_delete=models.PROTECT)
	# We don't store a key to the learning objective here since over time
	# the objectives may well change and we don't want to have to keep them
	# all linked in the database.  We can just collate the different values
	# we see for an individual course and present those.
	objective_text = models.CharField(max_length=255)
	
	def __str__(self):
		return objective_text+" score="+str(value)

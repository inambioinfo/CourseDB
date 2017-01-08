from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *

class CoursesView(generic.ListView):
	template_name = 'courses/courses.html'
	context_object_name = 'course_list'
	
	def get_queryset(self):
		return Course.objects.all()

class DiaryView(generic.ListView):
	pass

class CourseView(generic.DetailView):
	model = Course
	template_name = 'courses/course.html'


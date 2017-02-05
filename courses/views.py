from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.utils import timezone
from django import forms

class CoursesView(generic.ListView):
	template_name = 'courses/courses.html'
	context_object_name = 'course_list'
	
	def get_queryset(self):
		return Course.objects.all()

class DiaryView(generic.ListView):
	template_name = 'courses/diary.html'
	context_object_name = 'instances'

	def get_queryset(self):
		return CourseInstance.objects.filter(start_datetime__gte=timezone.now())
	
	
def CourseView(request, course_id):
	course = get_object_or_404(Course,pk=course_id)
	instances = course.courseinstance_set.filter(start_datetime__gte=timezone.now())
	
	return render(request, "courses/course.html", {
			'course': course,
			'instances': instances
	})
	
	
#class CourseView(generic.DetailView):
#	model = Course
#	template_name = 'courses/course.html'

class InstanceView(generic.DetailView):
	model = CourseInstance
	template_name = 'courses/instance.html'


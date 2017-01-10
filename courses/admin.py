from django.contrib import admin

from .models import Course, CourseInstance, Duration

admin.site.register(Course)
admin.site.register(CourseInstance)
admin.site.register(Duration)

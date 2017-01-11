from django.contrib import admin

from .models import Course, CourseInstance, Duration, LearningObjective

admin.site.register(Course)
admin.site.register(LearningObjective)
admin.site.register(CourseInstance)
admin.site.register(Duration)

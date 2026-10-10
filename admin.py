from django.contrib import admin
from .models import Course, Lesson, Enrollment, Question, Choice, Submission


class QuestionInline(admin.StackedInline):
    model = Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

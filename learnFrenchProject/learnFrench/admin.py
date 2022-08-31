from django.contrib import admin

# Register your models here.
from learnFrench.models import Answer, Question, Test, Lesson, Unit, Goal, DailyGoal


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer",)

    def has_add_permission(self, request):
        return True


admin.site.register(Answer, AnswerAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question",)

    def has_add_permission(self, request):
        return True


admin.site.register(Question, QuestionAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        return True


admin.site.register(Test, TestAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        return True


admin.site.register(Lesson, LessonAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        return True


admin.site.register(Unit, UnitAdmin)


class GoalAdmin(admin.ModelAdmin):
    list_display = ("goal",)

    def has_add_permission(self, request):
        return True


admin.site.register(Goal, GoalAdmin)


class DailyGoalAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True


admin.site.register(DailyGoal, DailyGoalAdmin)



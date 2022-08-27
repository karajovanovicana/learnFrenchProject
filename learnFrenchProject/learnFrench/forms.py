from django import forms

from learnFrench.models import DailyGoal, UserTest, UserTestView


class DailyGoalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DailyGoalForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = DailyGoal
        exclude = ("user", "date")
        labels = {
            "daily_goal": "Set daily goal"
        }

    def clean_daily_goal(self):
        daily_goal = self.cleaned_data.get('daily_goal')
        if not daily_goal:
            raise forms.ValidationError('This field is required')
        return daily_goal


class UserTestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserTestForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserTest
        exclude = ("user", "date", "completed")
        labels = {
            "user_test": "Perform the test"
        }


class UserTestViewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user_id')
        self.user = kwargs.pop('date')
        super(UserTestViewForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserTestView
        exclude = ("user_id", "comp_lessons", "daily_goal_id", "date")
        labels = {
            "comp_dg": "Check daily goal"
        }
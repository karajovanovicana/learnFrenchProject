from datetime import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from learnFrench.forms import DailyGoalForm, UserTestForm
from learnFrench.models import Unit, Lesson, Test, UserTestView


def home(request):
    queryset = Unit.objects.all()
    context = {"units": queryset}
    return render(request, "home.html", context=context)


def unit1(request):
    queryset = Unit.objects.all()[:1]
    context = {"units": queryset}
    return render(request, "unit.html", context=context)


def unit2(request):
    queryset = Unit.objects.all()[1:2]
    context = {"units": queryset}
    return render(request, "unit.html", context=context)

def unit3(request):
    queryset = Unit.objects.all()[2:3]
    context = {"units": queryset}
    return render(request, "unit.html", context=context)


def lesson1(request):
    queryset = Lesson.objects.all()[:1]
    context = {"lessons": queryset}
    return render(request, "lesson.html", context=context)


def lesson2(request):
    queryset = Lesson.objects.all()[1:2]
    context = {"lessons": queryset}
    return render(request, "lesson.html", context=context)


def lesson3(request):
    queryset = Lesson.objects.all()[2:3]
    context = {"lessons": queryset}
    return render(request, "lesson.html", context=context)


def lesson4(request):
    queryset = Lesson.objects.all()[3:4]
    context = {"lessons": queryset}
    return render(request, "lesson.html", context=context)

def lesson5(request):
    queryset = Lesson.objects.all()[4:5]
    context = {"lessons": queryset}
    return render(request, "lesson.html", context=context)


def profile(request):
    if request.method == "POST":
        form_data = DailyGoalForm(data=request.POST)
        if form_data.is_valid():
            daily_goal = form_data.save(commit=False)
            daily_goal.user = request.user
            daily_goal.date = datetime.now()
            daily_goal.save()
            return redirect("profile")
    queryset = User.objects.filter(username=request.user).all()
    queryset2 = UserTestView.objects.filter(username=request.user.username).filter(date=datetime.now()).distinct().all()

    context = {"user": queryset, "form": DailyGoalForm}
    context2 = {"daily_goal": queryset2, "form": DailyGoalForm}
    if queryset2.count() > 0:
        return render(request, "profile.html", context=context2)
    else:
        return render(request, "profile.html", context=context)


def test1(request):
    queryset = Test.objects.filter().all()[:1]
    context = {"tests": queryset}
    if request.method == "POST":
        form_data = UserTestForm(data=request.POST)
        if form_data.is_valid():
            user_test = form_data.save(commit=False)
            user_test.user = request.user
            user_test.date = datetime.now()
            user_test.completed = 1
            user_test.user_test_id = 1
            user_test.save()
            return redirect("home")
    return render(request, "usertest.html", context=context)


def test2(request):
    queryset = Test.objects.filter().all()[1:2]
    context = {"tests": queryset}
    if request.method == "POST":
        form_data = UserTestForm(data=request.POST)
        if form_data.is_valid():
            user_test = form_data.save(commit=False)
            user_test.user = request.user
            user_test.date = datetime.now()
            user_test.completed = 1
            user_test.user_test_id = 2
            user_test.save()
            return redirect("home")
    return render(request, "usertest.html", context=context)


def test3(request):
    queryset = Test.objects.filter().all()[2:3]
    context = {"tests": queryset}
    if request.method == "POST":
        form_data = UserTestForm(data=request.POST)
        if form_data.is_valid():
            user_test = form_data.save(commit=False)
            user_test.user = request.user
            user_test.date = datetime.now()
            user_test.completed = 1
            user_test.user_test_id = 3
            user_test.save()
            return redirect("home")
    return render(request, "usertest.html", context=context)


def test4(request):
    queryset = Test.objects.filter().all()[3:4]
    context = {"tests": queryset}
    if request.method == "POST":
        form_data = UserTestForm(data=request.POST)
        if form_data.is_valid():
            user_test = form_data.save(commit=False)
            user_test.user = request.user
            user_test.date = datetime.now()
            user_test.completed = 1
            user_test.user_test_id = 4
            user_test.save()
            return redirect("home")
    return render(request, "usertest.html", context=context)


def test5(request):
    queryset = Test.objects.filter().all()[4:5]
    context = {"tests": queryset}
    if request.method == "POST":
        form_data = UserTestForm(data=request.POST)
        if form_data.is_valid():
            user_test = form_data.save(commit=False)
            user_test.user = request.user
            user_test.date = datetime.now()
            user_test.completed = 1
            user_test.user_test_id = 5
            user_test.save()
            return redirect("home")
    return render(request, "usertest.html", context=context)

def instruction_manual(request):
    return render(request, "instruction-manual.html")


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/home/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/login")

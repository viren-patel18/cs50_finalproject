from django.shortcuts import render
import json
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta, date
from .models import *
from .forms import EmployeeForm

@login_required(login_url='/login')
def index(request):
    announcements = Announcement.objects.all().order_by("-id")
    maxDate = date.today() + timedelta(days=10)
    leaveRequests = LeaveRequest.objects.filter(dateFrom__lt = maxDate)
    return render(request, "django_hr/index.html", {
            'appName': 'HR Portal',
            'announcements': announcements,
            'leaveRequests': leaveRequests
    })

@login_required(login_url='/login')
def profile(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if employee is not None:
        return render(request, "django_hr/profile.html", {
            'employee': employee
        })
    return

def people(request):
    return render(request, "django_hr/people.html", {
        'employeeList': Employee.objects.all()
    })

def addEmployee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "django_hr/people.html", {
          'employeeList': Employee.objects.all()
        }) 

    return render(request, "django_hr/addEmployee.html", {
        'form': form
    })

def editEmployee(request, employee_id):
    if request.method == "POST":
        instance = Employee.objects.get(pk=employee_id)
        form = EmployeeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("profile", args=(instance.id,)))

    if employee_id is not None:
        instance = Employee.objects.get(pk=employee_id)
        form = EmployeeForm(None, instance=instance)

    return render(request, "django_hr/addEmployee.html", {
        'form': form    
    })

def timeOff(request):
    if request.method == "POST":
        leaveTypeRequest = request.POST["leaveType"]
        if leaveTypeRequest == "VACATION":
            leaveType = "PTO"
        elif leaveTypeRequest == "SICK":
            leaveType = "SL"
        else:
            leaveType = "UTO"
        dateFrom = datetime.datetime.strptime(request.POST["dateFrom"], "%Y-%m-%d").date()
        dateTo = datetime.datetime.strptime(request.POST["dateTo"], "%Y-%m-%d").date()
        days = (dateTo - dateFrom).days + 1
        leaveRequest = LeaveRequest(
            employee = request.user.employee,
            leaveType = leaveType,
            days = days,
            # vacationDays = days if leaveType == "VACATION" else 0,
            # sickDays = days if leaveType == "SICK" else 0,
            # unpaidDays = days if leaveType == "UNPAID" else 0,
            dateFrom = dateFrom,
            dateTo = dateTo,
            employeeComment = request.POST["comment"],
            status = "P"
        )
        leaveRequest.save()
        return HttpResponseRedirect(reverse("timeOff"))

    doneRequests = LeaveRequest.objects.filter(employee=request.user.employee).order_by("-id")
    return render(request, "django_hr/timeOff.html", {
        'doneRequests': doneRequests,
        'showName': False,
        'sickDays': request.user.employee.sickDays,
        'vacationDays': request.user.employee.vacationDays
    })

def leaveRequests(request):
    pendingRequests = LeaveRequest.objects.filter(status="P")
    doneRequests = LeaveRequest.objects.exclude(status="P")
    return render(request, "django_hr/leaveRequests.html", {
        'pendingRequests': pendingRequests,
        'doneRequests': doneRequests,
        'showName': True
    })

@csrf_exempt
def updateLeaveRequest(request):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT method expected."}, status = 400)
    data = json.loads(request.body)
    leaveRequest = LeaveRequest.objects.get(pk=data.get("leaveRequestID"))
    leaveRequest.status = " " if data.get("status") == "A" else "R"
    leaveRequest.hrComment = data.get("hrComment")
    employee = Employee.objects.get(pk=leaveRequest.employee.id)
    if leaveRequest.status == "A":
        if leaveRequest.leaveType == "PTO":
            employee.vacationDays -= leaveRequest.days
            employee.save()
        elif leaveRequest.leaveType == "SL":
            employee.sickDays -= leaveRequest.days
            employee.save()
    leaveRequest.save()
    return JsonResponse({"message": f"Leave Request edited successfully. {leaveRequest}"}, status = 201)
       
@csrf_exempt
def makeAnnouncement(request):
    if request.method != "POST":
        return JsonResponse({"error": "PUT method expected."}, status = 400)
    data = request.POST
    announcement = Announcement(
        title = data.get('title'),
        content = data.get('content'),
        creator = request.user.employee
        # timestamp = datetime.datetime.now
    )
    announcement.save()
    return HttpResponseRedirect(reverse("index"))

@csrf_exempt
def objectives(request):
    if request.method == "POST":
        # data = json.loads(request.body)
        data = request.POST
        if data.get('submitType') == "addObjective":
            objective = Objective(
                title = data.get('title'),
                description = data.get('description'),
                employee = request.user.employee,
                deadline = data.get('deadline')
            )
            objective.save()
        if data.get('submitType') == "viewObjective":
            objective = Objective.objects.get(pk=data.get('objectiveID'))
            chcekIns = CheckIn.objects.filter(objective=objective).order_by("-id")
            return render(request, "django_hr/viewObjective.html", {
                'objective': objective,
                'checkIns': chcekIns
            })
        if data.get('submitType') == "checkIn":
            objective = Objective.objects.get(pk=data.get('objectiveID'))
            return render(request, "django_hr/checkIn.html", {
                'objective': Objective.objects.get(pk=data.get('objectiveID'))
            })
        if data.get('submitType') == "update":
            objective = Objective.objects.get(pk=data.get('objectiveID'))
            objective.progress = data.get('progress')
            objective.save()
            checkIn = CheckIn(
                objective = objective,
                description = data.get('description'),
                progress = data.get('progress')
            )
            checkIn.save()
            checkIns = CheckIn.objects.filter(objective=objective).order_by("-id")
            return render(request, "django_hr/viewObjective.html", {
                'objective': Objective.objects.get(pk=data.get('objectiveID')),
                'checkIns': checkIns
            })
    objectives = Objective.objects.filter(employee = request.user.employee).filter(progress__lt = 100).order_by("-id")
    doneObjectives = Objective.objects.filter(employee = request.user.employee).filter(progress = 100).order_by("-id")
    return render(request, "django_hr/objectives.html", {
        'objectives': objectives,
        'doneObjectives': doneObjectives
    })
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication successful
        if user is not None:
            employee = Employee.objects.filter(user = user).first()
            if employee is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "django_hr/login.html", {
                    "message": "This user is not associated to an Employee. Please contact HR or use /Admin to make association."
                })
        else:
            return render(request, "django_hr/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "django_hr/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = email
        
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "django_hr/register.html", {
                "message": "Passwords must match."
            })

        # Check Employee exists with entered email
        employee = Employee.objects.filter(email = email).first()
        if not employee:
            return render(request, "django_hr/register.html", {
                "message": "This email is not registered to an Employee. Please contact HR."
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "django_hr/register.html", {
                "message": "Username already taken."
            })
        
        employee.user = user
        employee.save()

        # Create Employee object
        # first = request.POST["first"]
        # last = request.POST["last"]
        # employee = Employee(user = user, first = first, last = last)
        # employee.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "django_hr/register.html")

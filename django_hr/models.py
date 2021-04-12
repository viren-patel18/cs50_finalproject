from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# class User(AbstractUser):
#     pass

class Employee(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    school = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    postalCode = models.CharField(max_length=6, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    hireDate = models.DateField(default=datetime.date.today, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    vacationDays = models.IntegerField(default=0, blank=True, null=True)
    sickDays = models.IntegerField(default=0, blank=True, null=True)
    department = models.ForeignKey('Department', blank=True, null=True, on_delete=models.CASCADE, related_name="employees")
    position = models.ForeignKey('Position', blank=True, null=True, on_delete=models.CASCADE, related_name="employees")
    manager = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, related_name="employees")
    hr = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first} {self.last}"

class LeaveRequest(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name="leaveRequests")
    # vacationDays = models.IntegerField(default=0)
    # sickDays = models.IntegerField(default=0)
    # unpaidDays = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    dateFrom =  models.DateField()
    dateTo = models.DateField()
    LEAVETYPE_CHOICES = (
        ('PTO', 'Paid Vacation'),
        ('SL', 'Sick Leave'),
        ('UTO', 'Unpaid Time Off')
    )
    leaveType = models.CharField(max_length=30, choices=LEAVETYPE_CHOICES)
    STATUS_CHOICES = (
        ('P', 'Pending Approval'),
        ('A', 'Approved'),
        ('R', 'Rejected')
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    employeeComment = models.CharField(max_length=500, null=True, blank=True)
    hrComment = models. CharField(max_length=500, null=True, blank=True)

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    creator = models.ForeignKey('Employee', blank=True, null=True, on_delete=models.CASCADE, related_name="announcements")
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class Department(models.Model):
    name = models.CharField(max_length=30)
    head = models.ForeignKey('Employee', blank=True, null=True, on_delete=models.CASCADE, related_name="department_head")

    def __str__(self):
        return f"{self.name}"

class Position(models.Model):
    title = models.CharField(max_length=30)
    vacancies = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

class Objective(models.Model):
    title= models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    deadline = models.DateField()
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='objectives')
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class CheckIn(models.Model):
    objective = models.ForeignKey('Objective', on_delete=models.CASCADE, related_name='checkIns')
    description = models.CharField(max_length=500)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    

# @receiver(post_save, sender=User)
# def create_user_employee(sender, instance, created, **kwargs):
#     if created:
#         Employee.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_employee(sender, instance, **kwargs):
#     instance.Employee.save()

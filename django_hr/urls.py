from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:employee_id>", views.profile, name="profile"),
    path("people", views.people, name="people"),
    path("addEmployee", views.addEmployee, name="addEmployee"),
    path("editEmployee/<int:employee_id>", views.editEmployee, name="editEmployee"),
    path("timeOff", views.timeOff, name="timeOff"),
    path("leaveRequests", views.leaveRequests, name="leaveRequests"),
    path("updateLeaveRequest", views.updateLeaveRequest, name="updateLeaveRequest"),
    path("makeAnnouncement", views.makeAnnouncement, name="makeAnnouncement"),
    path("objectives", views.objectives, name="objectives")
]

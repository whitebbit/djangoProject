from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("student/<int:student_id>/", views.student_edit, name="student_edit"),
    path("student/", views.student_edit, name="student_add"),
    path(
        "student/delete/<int:student_id>/", views.student_delete, name="student_delete"
    ),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teacher/<int:teacher_id>/", views.teacher_edit, name="teacher_edit"),
    path("teacher/", views.teacher_edit, name="teacher_add"),
    path(
        "teacher/delete/<int:teacher_id>/", views.teacher_delete, name="teacher_delete"
    ),
    path("groups/", views.group_list, name="group_list"),
    path("group/<int:group_id>/", views.group_edit, name="group_edit"),
    path("group/", views.group_edit, name="group_add"),
    path("group/delete/<int:group_id>/", views.group_delete, name="group_delete"),
    path("send-sms/", views.send_sms, name="send_sms"),
]

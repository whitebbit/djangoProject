from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from faker import Faker

from myapp.forms import TeacherForm, GroupForm, StudentForm, PhoneNumberForm
from myapp.models import Student, Teacher, Group
from myapp.tasks import send_sms


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date(),
    )
    return HttpResponse("Student generated and saved.")


def generate_students(request):
    count = request.GET.get("count", 1)

    try:
        count = int(count)
        if count <= 0 or count > 100:
            return JsonResponse(
                {
                    "error": "Invalid count. Count should be a positive integer up to 100."
                },
                status=400,
            )
    except ValueError:
        return JsonResponse(
            {"error": "Invalid count. Count should be a positive integer up to 100."},
            status=400,
        )

    fake = Faker()
    students = []
    for _ in range(count):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date(),
        )
        students.append(student)

    Student.objects.bulk_create(students)
    return HttpResponse(f"{count} students generated and saved.")


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teacher_list.html", {"teachers": teachers})


def teacher_edit(request, teacher_id=None):
    if teacher_id:
        teacher = Teacher.objects.get(pk=teacher_id)
    else:
        teacher = None

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    else:
        form = TeacherForm(instance=teacher)

    return render(
        request, "teachers/teacher_edit.html", {"form": form, "teacher": teacher}
    )


def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return redirect("teacher_list")
    return redirect("teacher_list")


def student_list(request: object) -> object:
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})


def student_edit(request, student_id=None):
    if student_id:
        student = Student.objects.get(pk=student_id)
    else:
        student = None

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(
        request, "students/student_edit.html", {"form": form, "student": student}
    )


def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return redirect("student_list")


def group_list(request):
    groups = Group.objects.all()
    return render(request, "groups/group_list.html", {"groups": groups})


def group_edit(request, group_id=None):
    if group_id:
        group = Group.objects.get(pk=group_id)
    else:
        group = None

    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("group_list")
    else:
        form = GroupForm(instance=group)

    return render(request, "groups/group_edit.html", {"form": form, "group": group})


def group_delete(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        group.delete()
        return redirect("group_list")
    return redirect("group_list")


def send_sms(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            message = "Test message from django with celery"

            send_sms.delay(phone, message)
    else:
        form = PhoneNumberForm()

    return render(request, "sms_form.html", {"form": form})

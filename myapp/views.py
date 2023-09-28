from django.shortcuts import HttpResponse
from django.http import JsonResponse
from faker import Faker
from myapp.models import Student


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date(),
    )
    return HttpResponse("Student generated and saved.")


def generate_students(request):
    count = request.GET.get('count', 1)

    try:
        count = int(count)
        if count <= 0 or count > 100:
            return JsonResponse({'error': 'Invalid count. Count should be a positive integer up to 100.'}, status=400)
    except ValueError:
        return JsonResponse({'error': 'Invalid count. Count should be a positive integer up to 100.'}, status=400)

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

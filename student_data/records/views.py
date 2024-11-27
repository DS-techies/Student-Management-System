from django.shortcuts import render, redirect
from .models import Student, Attendance
from django.utils import timezone

def mark_attendance(request):
    if request.method == "POST":
        for student_id in request.POST.getlist('students'):
            status = request.POST.get(f'student_{student_id}') == 'on'
            Attendance.objects.update_or_create(
                student_id=student_id,
                date=timezone.now().date(),
                defaults={'status': status}
            )
        return redirect('mark_attendance')

    students = Student.objects.all()
    return render(request, 'mark_attendance.html', {'students': students})

def view_attendance(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        records = Attendance.objects.filter(student_id=student_id).order_by('date')
        student_name = Student.objects.get(id=student_id).name
        return render(request, 'view_attendance.html', {'records': records, 'student_name': student_name})

    students = Student.objects.all()
    return render(request, 'view_attendance.html', {'students': students})
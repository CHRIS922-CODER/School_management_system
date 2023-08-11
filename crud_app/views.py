from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *


def home(request):
    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list') 
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)  
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  
    return render(request, 'delete_student.html', {'student': student})


def unit_list(request):
    units = Unit.objects.all()
    return render(request,'unit_list.html',{'units':units})

def add_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
        else:
            print('error: ',form.errors)
    else:
        form = UnitForm()
    return render(request,'add_unit.html',{'form':form})
def edit_unit(request,pk):
    unit = get_object_or_404(Unit,pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_detail')
    else:
        form = UnitForm(instance=unit)
    return render(request, 'edit_unit.html',{'form':form,'unit':unit})

def delete_unit(request,pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('unit_list')
    return render(request,'delete_unit.html',{'unit':unit})


def course_list(request):
    courses = Course.objects.all()
    return render(request,'course_list.html',{'courses':courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request,'add_course.html',{'form':form})

def edit_course(request,pk):
    course = get_object_or_404(Course,pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html',{'form':form,'course':course})

def delete_course(request,pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request,'delete_course.html',{'course':course})


def marks_list(request):
    students = StudentMarks.objects.all().order_by('-id')
    print(students)
    return render(request,'marks_list.html',{'students':students})

def enroll(request,pk):
    student = Student.objects.get(pk=pk)
    print(student)
    student.enrolled = True
    student.save()
    return redirect('enrolled_list')

def enrolled_list(request):
    students = Student.objects.filter(enrolled=True).order_by('-id')
    return render(request,'enrolled_list.html',{'students':students})

def add_marks(request, pk,unit_code):
    student = get_object_or_404(Student, pk=pk,unit_code=unit_code)
    

    if request.method == 'POST':
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            student_marks = form.save(commit=False)  # Create but don't save instance yet
            student_marks.student = student 
            student_marks.unit_code = form.cleaned_data['unit_code']  
            student_marks.save()
            student.graded = True
            student.save()
            return redirect('marks_list')
    else:
        form = StudentMarksForm()

    return render(request, 'add_marks.html', {'form': form, 'student': student,'unit_code':unit_code})

    
def edit_marks(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        form = StudentMarksForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('marks_list')
    else:
        form = StudentMarksForm(instance=student)
    return render(request, 'edit_marks.html',{'form':form,'student':student})

def delete_marks(request,pk):
    marks = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        marks.delete()
        return redirect('marks_list')
    return render(request,'delete_marks.html',{'marks':marks})

from django.http import JsonResponse

def toggle_enrollment(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(pk=student_id)
            student.enrolled = not student.enrolled
            student.save()
            return JsonResponse({'enrolled': student.enrolled})
        except Student.DoesNotExist:
            pass
    return JsonResponse({'error': 'Invalid request'}, status=400)



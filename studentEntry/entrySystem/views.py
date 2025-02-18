from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .form import StudentForm
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
        else:
            return render(request, "new.html", {"form": form})
    else:
        form = StudentForm()
        return render(request, "new.html", {"form": form})
    
def student_update(request, id):
    student = get_object_or_404(Student, pk=id)
    update_successful = False

    if request.method == 'POST' and request.POST.get('_method') == 'PATCH':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            update_successful = True
            return render(request, 'update.html', {'form': form, 'student': student, 'update_successful': update_successful})

    else:
        form = StudentForm(instance=student)

    return render(request, 'update.html', {'form': form, 'student': student, 'update_successful': update_successful})


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete.html', {'student': student})

def student_detail(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'student_detail.html', {'student': student})
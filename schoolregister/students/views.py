from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from students.models import Student
from students.models import StudentNote

# Create your views here.
def student_listing(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_listing.html', context)

def student_details(request, student_id):

    # this view renders student details and all notes saved to the student.
    student = Student.objects.get(pk=student_id)
    
    # if a new note is added, we recieve the actual text in the request POTS dictionary
    if request.method == "POST":
        # So to get the new note text, do this:
        new_note_text = request.POST.get('new_note')
        # Make a new intance of the StudentNote model
        new_note = StudentNote()
        # Set the new note "note" text to the one we got from request.POST
        new_note.note = new_note_text
        # Set the new note student reference to the student in question
        new_note.student = student
        # Save the user that actually created this note
        new_note.created_by = request.user
        # Set the time for the saving of the new note
        new_note.created_datetime = timezone.now()
        # Now we need Django to save info on the new note to the database.
        # We do it like this
        new_note.save()



    context = {'student': student}
    return render(request, 'students/student_details.html', context)

def student_increase_passed_exams(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.passed_exams = student.passed_exams + 1
    student.save()
    data = {'passed_exams_updated': student.passed_exams}
    return JsonResponse(data)
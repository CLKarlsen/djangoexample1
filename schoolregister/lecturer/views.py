from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from lecturer.models import Lecturer
# Create your views here.

def lecturer_listing(request):
    lecturer = Lecturer.objects.all()
    context = {'lecturer': lecturer}
    return render(request, 'lecturer/lecturer_listing.html', context)

def lecturer_detail(request, lecturer_id):
    lecturer = Lecturer.objects.get(pk=lecturer_id)
    context = {'lecturer': lecturer}
    return render(request, 'lecturer/lecturer_detail.html', context)

def lecturer_increase_number_of_courses(request, lecturer_id):
    lecturer = Lecturer.objects.get(pk=lecturer_id)
    lecturer.number_of_courses = lecturer.number_of_courses + 1
    lecturer.save()
    data = {'number_of_courses_updated': lecturer.number_of_courses}
    return JsonResponse(data)

def lecturer_decrease_number_of_courses(request, lecturer_id):
    lecturer = Lecturer.objects.get(pk=lecturer_id)
    lecturer.number_of_courses = lecturer.number_of_courses - 1
    lecturer.save()
    data = {'number_of_courses_updated': lecturer.number_of_courses}
    return JsonResponse(data)

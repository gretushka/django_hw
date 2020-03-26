from django.views.generic import ListView
from django.shortcuts import render
import json
from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    path = 'school.json'
    with open(path, 'r') as jsonfile:
        data = json.loads(jsonfile.read())
        for line in data:
            if line['model'] == "school.teacher":
                if Teacher.objects.filter(id=line['pk']):
                    pass
                else:
                    Teacher.objects.create(name=line['fields']['name'],
                                         subject=line['fields']['subject'],
                                         )
            else:
                if Student.objects.filter(id=line['pk']):
                    pass
                else:
                    teacher = Teacher.objects.get(id = line['fields']['teacher'])
                    print(teacher)
                    student = Student.objects.create(name=line['fields']['name'],
                                           group=line['fields']['group']
                    )
                    student.teachers.add(teacher)
                    student.save()
    students = Student.objects.prefetch_related('teachers').order_by("group")
    context = {
        'object_list': students,
    }


    return render(request, template, context)

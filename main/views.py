from django.shortcuts import render

from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Raihan",
        "fullname": "Raihan Daffa Aprilianda",
        "npm": "2506620021",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia currently on my 3rd semester. "
            "Wishing to be good at programming someday."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Raihan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    context = {
        "name": "Raihan",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import Student
from django.urls import reverse


class CreateStudent(CreateView):
    model = Student
    fields = ['name', 'birthdate']
    template_name = 'student/create.html'

    def get_success_url(self):
        return reverse('home')


class ListStudent(ListView):
    model = Student
    template_name = 'student/list.html'


class UpdateStudent(UpdateView):
    model = Student
    fields = ['name', ]
    template_name = 'student/create.html'

    def get_success_url(self):
        return reverse('list-student')


class DetailStudent(DetailView):
    model = Student
    template_name = 'student/detail.html'

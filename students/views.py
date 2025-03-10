from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Student
from .forms import StudentForm

# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        return Student.objects.filter(is_active=True)
    
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
    
class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')
    success_message = "Student '%(name)s' was created successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Student'
        context['submit_text'] = 'Add Student'
        return context
    
class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')
    success_message = "Student '%(name)s' was updated successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student'
        context['submit_text'] = 'Update Student'
        return context
    
class StudentDeleteView(SuccessMessageMixin, DetailView):
    model = Student
    template_name = 'student_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student-list')
    success_message = "Student was deleted successfully!"
    
    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, f"Student '{student.name}' was deleted successfully!")
        return super().delete(request, *args, **kwargs)
    
    
    
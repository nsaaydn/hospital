from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient
from .forms import PatientForm

class PatientListView(ListView):
    model = Patient
    template_name = 'patient/patient_list.html'
    context_object_name = 'patients' 
    ordering = ['first_name'] 

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient' 
    pk_url_kwarg = 'patient_id'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        messages.success(self.request, 'Patient added successfully.')
        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient:patient_list') 
    pk_url_kwarg = 'patient_id' 


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/patient_confirm_delete.html' 
    success_url = reverse_lazy('patient:patient_list')
    pk_url_kwarg = 'patient_id' 
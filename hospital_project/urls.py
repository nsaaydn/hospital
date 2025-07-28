# hospital_project/urls.py

from django.contrib import admin
from django.urls import path
from patient import views     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/<int:patient_id>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patients/add/', views.PatientCreateView.as_view(), name='patient_add'),
    path('patients/<int:patient_id>/edit/', views.PatientUpdateView.as_view(), name='patient_edit'),
    path('patients/<int:patient_id>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),
]
from django.views.generic import ListView, DetailView

from patient.models import Patient

class PatientListView(ListView):
    model = Patient
    queryset = Patient.objects.order_by('-subject_number')


class PatientView(DetailView):
    model = Patient

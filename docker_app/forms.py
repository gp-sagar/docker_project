from django import forms
from .models import student


class StudentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = (
            'first_name',
            'last_name',
            'age',
            'city',
        )
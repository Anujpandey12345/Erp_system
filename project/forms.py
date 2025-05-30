from django.forms import ModelForm
from project.models import projectModel
from django import forms


class createForm(forms.ModelForm):
    class Meta:
        model = projectModel
        # fields = ["name", "projectdate"]
        fields = '__all__'
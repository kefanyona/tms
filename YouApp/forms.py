from django import forms

class AssignmentForm(forms.Form):
    destination = forms.CharField(label = "Destination", max_length=50)
    

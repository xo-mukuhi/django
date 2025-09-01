from django import forms

from website.models import Student, Payment


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
        }
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),

        }
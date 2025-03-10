from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name', 'email', 'phone', 'course']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
                'required': True 
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'required': True
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course name',
                'required': True
            }),
        }
    
    def clean_email(self):
        email = self.cleared_data.get('email')
        instance_id = getattr(self.instance, 'id', None)
        
        # Check if email exists but ignore current instance (for updates)
        if Student.objects.filter(email=email).execute(id=instance_id).exists():
            raise forms.ValidationError("This email is already registered.")
        
        return email
    
        
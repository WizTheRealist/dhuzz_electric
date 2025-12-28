from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from .models import ContactMessage, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary transition-all',
                'placeholder': 'John Doe'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary transition-all',
                'placeholder': 'john@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary transition-all',
                'placeholder': '+234...'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary transition-all resize-none',
                'placeholder': 'How can we help you with your electrical needs?',
                'rows': 5
            }),
        }


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'phone', 'service_type', 'location', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none',
                'placeholder': 'your.email@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none',
                'placeholder': '+234 XXX XXX XXXX'
            }),
            'service_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none',
                'placeholder': 'e.g., Lekki, Lagos'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-dark-bg border border-white/10 rounded-xl focus:border-primary focus:outline-none resize-none',
                'placeholder': 'Please describe your electrical needs...',
                'rows': 4
            }),
        }
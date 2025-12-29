from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Service(models.Model):
    SERVICE_TYPES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('industrial', 'Industrial'),
        ('emergency', 'Emergency'),
        ('solar', 'Solar & Inverter'),
        ('maintenance', 'Maintenance'),
    ]
    
    title = models.CharField(max_length=200)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='bolt')
    image = CloudinaryField('service_image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title


class Project(models.Model):
    PROJECT_TYPES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('industrial', 'Industrial'),
        ('solar', 'Solar'),
    ]
    
    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('project_image')
    completion_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100)
    client_image = CloudinaryField('testimonial_image', blank=True, null=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"


class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('residential', 'Residential Wiring'),
        ('commercial', 'Commercial Installation'),
        ('lighting', 'Lighting Design'),
        ('emergency', 'Emergency Repair'),
        ('solar', 'Solar & Inverter'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    location = models.CharField(max_length=200)
    description = models.TextField()
    is_contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.service_type}"
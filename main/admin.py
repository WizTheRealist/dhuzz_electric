from django.contrib import admin
from .models import Service, Project, Testimonial, ContactMessage, QuoteRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'service_type', 'is_active', 'order']
    list_filter = ['service_type', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'location', 'is_featured', 'completion_date']
    list_filter = ['project_type', 'is_featured']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_featured']
    date_hierarchy = 'completion_date'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured']
    search_fields = ['client_name', 'review']
    list_editable = ['is_featured']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'location', 'is_contacted', 'created_at']
    list_filter = ['service_type', 'is_contacted', 'created_at']
    search_fields = ['name', 'email', 'location', 'description']
    list_editable = ['is_contacted']
    readonly_fields = ['created_at']

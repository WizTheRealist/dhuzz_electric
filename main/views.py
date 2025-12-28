from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic import TemplateView, ListView
from .models import Service, Project, Testimonial, ContactMessage
from .forms import ContactForm, QuoteRequestForm

def home(request):
    services = Service.objects.filter(is_active=True)[:3]
    projects = Project.objects.filter(is_featured=True)[:3]
    testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'page': 'home'
    }
    return render(request, 'home.html', context)


def services(request):
    all_services = Service.objects.filter(is_active=True)
    context = {
        'services': all_services,
        'page': 'services'
    }
    return render(request, 'services.html', context)


def projects(request):
    all_projects = Project.objects.all()
    project_type = request.GET.get('type', 'all')
    
    if project_type != 'all':
        all_projects = all_projects.filter(project_type=project_type)
    
    context = {
        'projects': all_projects,
        'selected_type': project_type,
        'page': 'projects'
    }
    return render(request, 'projects.html', context)


def about(request):
    context = {'page': 'about'}
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification
            try:
                subject = f"New Contact Message from {contact_message.name}"
                message = f"""
                Name: {contact_message.name}
                Email: {contact_message.email}
                Phone: {contact_message.phone}
                
                Message:
                {contact_message.message}
                """
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            except Exception as e:
                messages.warning(request, 'Message saved but email notification failed.')
            
            messages.success(request, 'Thank you for your message! We will get back to you within 24 hours.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page': 'contact'
    }
    return render(request, 'contact.html', context)


def request_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            
            # Send email notification
            try:
                subject = f"New Quote Request from {quote.name}"
                message = f"""
                Name: {quote.name}
                Email: {quote.email}
                Phone: {quote.phone}
                Service Type: {quote.get_service_type_display()}
                Location: {quote.location}
                
                Description:
                {quote.description}
                """
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception:
                pass
            
            messages.success(request, 'Quote request submitted! We will contact you soon.')
            return redirect('home')
    else:
        form = QuoteRequestForm()
    
    return render(request, 'quote.html', {'form': form})

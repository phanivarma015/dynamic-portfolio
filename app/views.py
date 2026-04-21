from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Profile, Education, Experience, Project,
    SkillCategory, Certification, Language, ContactMessage
)


def home(request):
    """Main single-page portfolio view."""
    profile = Profile.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    certifications = Certification.objects.all()
    languages = Language.objects.all()

    context = {
        'profile': profile,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'skill_categories': skill_categories,
        'certifications': certifications,
        'languages': languages,
    }
    return render(request, 'app/index.html', context)


def contact(request):
    """Handle contact form submission."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            messages.success(request, 'Your message has been sent! I will get back to you soon.')
        else:
            messages.error(request, 'Please fill in all fields.')

    return redirect('home')

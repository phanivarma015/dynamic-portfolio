from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, Education, Experience, Project,
    SkillCategory, Skill, Certification, Language, ContactMessage
)

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Panel"
admin.site.index_title = "Welcome to Portfolio Dashboard"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'location')
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'title', 'bio', 'photo')}),
        ('Contact', {'fields': ('email', 'location')}),
        ('Links', {'fields': ('github_url', 'linkedin_url', 'resume')}),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'cgpa', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'duration', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'order', 'github_link')
    list_editable = ('featured', 'order')
    list_filter = ('featured',)
    ordering = ('order',)

    def github_link(self, obj):
        if obj.github_url:
            return format_html('<a href="{}" target="_blank">GitHub ↗</a>', obj.github_url)
        return '—'
    github_link.short_description = 'GitHub'


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'proficiency', 'order')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_editable = ('proficiency', 'order')
    list_filter = ('category',)
    ordering = ('category', 'order')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'year', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read',)
    list_editable = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

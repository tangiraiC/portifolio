from django.contrib import admin

# Register your models here.
# core/admin.py
from django.contrib import admin
from .models import (
    Category, Project, ResearchPaper, BlogPost, ProjectImage,
    Resume, Certification, ContactMessage, Experience, Education, Skill, SiteSetting
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)





class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "primary_category", "status", "created_at")
    list_filter = ("primary_category", "status")
    search_fields = ("title", "tags_csv", "tech_stack_csv")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]


@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "created_at")
    search_fields = ("title", "citation")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "created_at")
    search_fields = ("title", "tags_csv")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_primary", "version", "updated_at")
    list_filter = ("is_primary",)
    search_fields = ("title",)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "contact_email", "updated_at")

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuing_organization", "issue_date")
    search_fields = ("name",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency")
    list_filter = ("category",)
    search_fields = ("name",)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "is_current")
    list_filter = ("is_current",)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_date")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "created_at", "is_read")
    list_filter = ("is_read",)
    readonly_fields = ("created_at",)
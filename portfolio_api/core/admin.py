from django.contrib import admin

# Register your models here.
# core/admin.py
from django.contrib import admin
from .models import Category, Project, ResearchPaper, BlogPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "primary_category", "status", "created_at")
    list_filter = ("primary_category", "status")
    search_fields = ("title", "tags_csv", "tech_stack_csv")
    prepopulated_fields = {"slug": ("title",)}


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
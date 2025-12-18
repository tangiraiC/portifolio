from rest_framework import serializers
from .models import Category, Project, ResearchPaper, BlogPost, Resume, Certification, ContactMessage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='primary_category.name', read_only=True)
    category_slug = serializers.CharField(source='primary_category.slug', read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'primary_category', 'category_name', 'category_slug',
            'status', 'tags_csv', 'tech_stack_csv', 'highlights_csv',
            'abstract', 'repo_url', 'demo_url', 'start_date', 'end_date', 'cover_image'
        ]

class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
        read_only_fields = ['created_at']
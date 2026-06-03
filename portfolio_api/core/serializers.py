from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (

    Category, Project, ResearchPaper, BlogPost, Resume, Certification, ContactMessage,
    Experience, Education, Skill, SiteSetting, ProjectImage, Comment
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption', 'order']

class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='primary_category.name', read_only=True)
    category_slug = serializers.CharField(source='primary_category.slug', read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'primary_category', 'category_name', 'category_slug',
            'status', 'tags_csv', 'tech_stack_csv', 'highlights_csv',
            'abstract', 'repo_url', 'demo_url', 'start_date', 'end_date', 'cover_image',
            'images'
        ]

class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'guest_name', 'author_name', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']

    def get_author_name(self, obj):
        if obj.author:
            return obj.author.username
        return obj.guest_name or "Anonymous"

class BlogPostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count() + obj.anonymous_likes

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'published_at', 'author', 'hero_image', 
                  'body', 'tags_csv', 'is_published', 'likes_count', 'comments', 'is_liked', 'created_at']

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False

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

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
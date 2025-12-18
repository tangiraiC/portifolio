from rest_framework import viewsets, filters 
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Project, ResearchPaper, BlogPost, Resume, Certification, ContactMessage
from .serializers import (
    CategorySerializer, ProjectSerializer, ResearchPaperSerializer, 
    BlogPostSerializer, ResumeSerializer, CertificationSerializer, ContactMessageSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-start_date')
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'primary_category__slug']
    search_fields = ['title', 'tech_stack_csv', 'tags_csv']
    ordering_fields = ['start_date', 'title']

class ResearchPaperViewSet(viewsets.ModelViewSet):
    queryset = ResearchPaper.objects.all().order_by('-published_at')
    serializer_class = ResearchPaperSerializer
    search_fields = ['title', 'citation']

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    serializer_class = BlogPostSerializer
    search_fields = ['title', 'tags_csv']

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all().order_by('-is_primary', '-updated_at')
    serializer_class = ResumeSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all().order_by('-issue_date')
    serializer_class = CertificationSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
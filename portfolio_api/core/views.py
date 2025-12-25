from rest_framework import viewsets, filters 
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Category, Project, ResearchPaper, BlogPost, Resume, Certification, ContactMessage,
    Experience, Education, Skill, SiteSetting
)
from .serializers import (
    CategorySerializer, ProjectSerializer, ResearchPaperSerializer, 
    BlogPostSerializer, ResumeSerializer, CertificationSerializer, ContactMessageSerializer,
    ExperienceSerializer, EducationSerializer, SkillSerializer, SiteSettingSerializer,
    UserRegistrationSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.generics import CreateAPIView



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

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('-proficiency')
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name', 'category']

class SiteSettingViewSet(viewsets.ModelViewSet):
    """
    Since this is a singleton, we might want to restrict creation if one exists.
    But for MVP, standard ModelViewSet is okay, just be careful on frontend.
    """
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RegisterView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
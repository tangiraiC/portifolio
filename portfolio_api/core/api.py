from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProjectViewSet, ResearchPaperViewSet, 
    BlogPostViewSet, ResumeViewSet, CertificationViewSet, ContactMessageViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'research', ResearchPaperViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'resume', ResumeViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'contact', ContactMessageViewSet)

urlpatterns = router.urls
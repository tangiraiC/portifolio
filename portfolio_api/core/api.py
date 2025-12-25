from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProjectViewSet, ResearchPaperViewSet, 
    BlogPostViewSet, ResumeViewSet, CertificationViewSet, ContactMessageViewSet,
    ExperienceViewSet, EducationViewSet, SkillViewSet, SiteSettingViewSet,
    RegisterView
)



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'research', ResearchPaperViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'resume', ResumeViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'contact', ContactMessageViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'site-settings', SiteSettingViewSet)


urlpatterns = router.urls
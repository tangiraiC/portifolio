from django.db import models
from django.utils.text import slugify

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

def project_image_path(instance, filename):
    return f"projects/{instance.slug}/{filename}"

class Project(TimeStampedModel):
    STATUS_CHOICES = (
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    primary_category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="projects")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="in_progress")
    
    # Comma-separated or JSON list for simplicity in this MVP
    tags_csv = models.CharField(max_length=400, blank=True, help_text="comma-separated tags")
    tech_stack_csv = models.CharField(max_length=500, blank=True, help_text="comma-separated tech")
    
    highlights_csv = models.TextField(blank=True, help_text="one per line")
    
    abstract = models.TextField(blank=True)
    description = models.TextField(blank=True) # Full markdown content
    
    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    cover_image = models.ImageField(upload_to=project_image_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

def project_gallery_path(instance, filename):
    return f"projects/{instance.project.slug}/gallery/{filename}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=project_gallery_path)
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.project.title}"

def research_pdf_path(instance, filename):
    return f"research/{instance.slug}/{filename}"

class ResearchPaper(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    citation = models.TextField(blank=True)
    published_at = models.DateField(null=True, blank=True)
    pdf = models.FileField(upload_to=research_pdf_path, blank=True, null=True)
    link = models.URLField(blank=True)
    abstract = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

def blog_image_path(instance, filename):
    return f"blog/{instance.slug}/{filename}"

class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=100, default="Lincoln")
    
    hero_image = models.ImageField(upload_to=blog_image_path, blank=True, null=True)
    body = models.TextField(help_text="Markdown content")
    tags_csv = models.CharField(max_length=200, blank=True)
    
    is_published = models.BooleanField(default=False)
    
    # Interactions
    likes = models.ManyToManyField("auth.User", related_name="liked_posts", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(TimeStampedModel):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

def resume_pdf_path(instance, filename):
    return f"resume/{filename}"

class Resume(TimeStampedModel):
    title = models.CharField(max_length=100, help_text="e.g. 'Software Engineer Resume 2024'")
    pdf = models.FileField(upload_to=resume_pdf_path)
    is_primary = models.BooleanField(default=False, help_text="If checked, this will be the main download.")
    version = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if self.is_primary:
            # maintain one primary
            Resume.objects.exclude(id=self.id).update(is_primary=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

def certification_image_path(instance, filename):
    return f"certifications/{filename}"

class Certification(TimeStampedModel):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to=certification_image_path, blank=True, null=True)

    def __str__(self):
        return self.name

class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}: {self.subject}"

class Experience(TimeStampedModel):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Markdown content")
    
    def __str__(self):
        return f"{self.role} at {self.company}"
        
    class Meta:
        ordering = ['-start_date']

class Education(TimeStampedModel):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, help_text="Markdown content")
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"
        
    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-start_date']

class Skill(TimeStampedModel):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="1-100", default=50)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, help_text="e.g., Frontend, Backend, Tools")
    
    def __str__(self):
        return self.name

class SiteSetting(TimeStampedModel):
    about_me = models.TextField(blank=True, help_text="Markdown content for About Me section")
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="Upload PDF resume (overrides external link)")
    resume_link = models.URLField(blank=True, help_text="External link to resume if not hosted here")
    contact_email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSetting.objects.exists():
            # If valid instance exists, update it instead of creating new? 
            # Or just enforce singleton pattern. For now, simple check.
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return "Site Settings"
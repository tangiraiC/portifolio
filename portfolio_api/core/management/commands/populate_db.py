from django.core.management.base import BaseCommand
from core.models import Project, Category, BlogPost
from datetime import date
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        # 1. Categories
        categories = [
            ("Web Development", "Web apps and sites"),
            ("AI & Machine Learning", "AI/ML Projects"),  # Changed 'and' to '&'
            ("Business & Data Analytics", "Data Viz and Business Logic"), # Changed 'and' to '&'
            ("Hackathons", "Hackathon Projects"),
            ("Writing", "Blog posts and articles"),
        ]

        cat_objs = {}
        for name, desc in categories:
            # Safe Rename/Merge Logic
            old_name = name.replace("&", "and") 
            
            # Only proceed if we are actually renaming something
            if old_name != name and Category.objects.filter(name=old_name).exists():
                # 1. Check if the "New Name" (target) ALSO exists
                if Category.objects.filter(name=name).exists():
                    # Both exist. Move projects from Old to New, then delete Old.
                    old_cat = Category.objects.get(name=old_name)
                    new_cat = Category.objects.get(name=name)
                    Project.objects.filter(primary_category=old_cat).update(primary_category=new_cat)
                    old_cat.delete()
                    self.stdout.write(f'Merged category "{old_name}" into "{name}"')
                else:
                    # Only Old exists. Rename it.
                    Category.objects.filter(name=old_name).update(name=name)
                    self.stdout.write(f'Renamed category "{old_name}" to "{name}"')

            cat, created = Category.objects.get_or_create(name=name, defaults={"description": desc})
            cat_objs[name] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Category: {name}'))
            else:
                self.stdout.write(f'Category confirmed: {name}')

        # 2. Projects
        # Neural Agent (The Shona Request)
        shona_slogan = "Tiri mubhizimusi rekuvandudza mienzaniso" # "We are in the business of optimizing models"
        neural_desc = f"""
```python
class NeuralAgent(nn.Module):
  def __init__(self, data):
    self.architecture = ["Transformer", "LSTM"]
    self.objective = "{shona_slogan}"
  def forward(self, x):
    return predict_future(x)
```
        """
        
        Project.objects.update_or_create(
            title="Neural Agent Optimization",
            defaults={
                "slug": "neural-agent-optimization",
                "primary_category": cat_objs["Business & Data Analytics"],
                "status": "completed",
                "tags_csv": "Python, PyTorch, LSTM, Transformer",
                "tech_stack_csv": "Python, PyTorch",
                "abstract": f"An advanced neural agent optimized for business objectives. Slogan: {shona_slogan}",
                "description": neural_desc, # Markdown
                "repo_url": "https://github.com/lincoln/neural-agent",
                "start_date": date(2024, 1, 1),
                "cover_image": None # Optional
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: Neural Agent'))

        # Standard E-Commerce
        Project.objects.update_or_create(
            title="E-Commerce Platform",
            defaults={
                "slug": "ecommerce-platform",
                "primary_category": cat_objs["Web Development"],
                "status": "completed",
                "tags_csv": "Vue.js, Django, Postgres",
                "tech_stack_csv": "Vue.js, Python, PostgreSQL, Docker",
                "abstract": "A scalable e-commerce platform with real-time inventory management.",
                "repo_url": "https://github.com/example/ecommerce",
                "demo_url": "https://demo.example.com",
                "start_date": date(2024, 1, 15)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: E-Commerce'))

        # AI Image Classifier
        Project.objects.update_or_create(
            title="AI Image Classifier",
            defaults={
                "slug": "ai-image-classifier",
                "primary_category": cat_objs["AI & Machine Learning"],
                "status": "completed",
                "tags_csv": "PyTorch, React, API",
                "tech_stack_csv": "Python, PyTorch, React, FastAPI",
                "abstract": "Deep learning model for classifying detailed image datasets with 98% accuracy.",
                "repo_url": "https://github.com/example/image-classifier",
                "start_date": date(2023, 11, 10)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: AI Image Classifier'))

        # FIFA Wage Analysis
        Project.objects.update_or_create(
            title="FIFA Wage Analysis",
            defaults={
                "slug": "fifa-wage-analysis",
                "primary_category": cat_objs["Business & Data Analytics"],
                "status": "completed",
                "tags_csv": "Data Analysis, Statistics, Hypothesis Testing",
                "tech_stack_csv": "R, Python, Pandas, SciPy", 
                "abstract": "Statistical analysis of wage differences between Brazilian and Spanish FIFA substitutes.",
                "description": """
### Overview
This project analyzes wage disparities between Brazilian and Spanish soccer players categorized as substitutes. 

**Key Findings:**
- Checked assumption of equal variances (Variance Test).
- Performed T-Test (alpha 0.05).
- Investigated if nationality influences compensation for substitute players.
                """,
                "repo_url": "https://github.com/tangiraiC/Analysis-of-Wage-Differences-Among-Brazilian-and-Spanish-FIFA-Substitutes",
                "start_date": date(2023, 6, 1)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: FIFA Analysis'))

        # SmartDine
        Project.objects.update_or_create(
            title="SmartDine",
            defaults={
                "slug": "smartdine",
                "primary_category": cat_objs["AI & Machine Learning"], # It's a recommender system
                "status": "completed",
                "tags_csv": "Recommender Systems, Multimodal AI, React, Django",
                "tech_stack_csv": "Python, Django, React, PyTorch, NLTK",
                "abstract": "A multimodal restaurant recommender system using text, image, and dense feature fusion.",
                "description": """
### Features
- **Multimodal Embeddings**: Fuses text, image, and dense features.
- **Algorithms**: Matrix Factorization, Neural Collaborative Filtering, Late Fusion, Joint Embedding.
- **Architecture**: Django REST API serving a React frontend.
- **Real-time**: Precomputed item-level caches for efficient serving.
                """,
                "repo_url": "https://github.com/tangiraiC/smartdine",
                "start_date": date(2025, 1, 1) # Based on citation year
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: SmartDine'))

        # Resume Optimizer
        Project.objects.update_or_create(
            title="Resume Optimizer",
            defaults={
                "slug": "resume-optimizer",
                "primary_category": cat_objs["Web Development"], 
                "status": "completed",
                "tags_csv": "Flask, NLP, Career Tools",
                "tech_stack_csv": "Python, Flask, HTML/CSS, PDF Generation",
                "abstract": "Flask-based web application for resume optimization and ATS-friendly formatting.",
                "description": """
### Overview
A web tool to help job seekers optimize their resumes.

**Features:**
- Resume optimization logic.
- HTML and PDF generation.
- ATS-friendly formatting standards.
                """,
                "repo_url": "https://github.com/tangiraiC/resume-optimizer",
                "start_date": date(2023, 11, 1)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: Resume Optimizer'))

        # The FlexForce API
        Project.objects.update_or_create(
            title="The FlexForce API",
            defaults={
                "slug": "theflexforceapi",
                "primary_category": cat_objs["Web Development"],
                "status": "completed",
                "tags_csv": "API, Backend, Gig Economy",
                "tech_stack_csv": "Django, Django REST Framework, PostgreSQL",
                "abstract": "Backend API for the FlexForce gig economy platform.",
                "repo_url": "https://github.com/tangiraiC/theflexforceapi", # Note: Link was 404, kept as provided
                "start_date": date(2023, 9, 20)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: FlexForce API'))

        # My Portfolio
        Project.objects.update_or_create(
            title="My Portfolio",
            defaults={
                "slug": "my-portfolio",
                "primary_category": cat_objs["Web Development"],
                "status": "completed",
                "tags_csv": "Personal Brand, Full Stack, Interactive",
                "tech_stack_csv": "Django, Vue.js, TailwindCSS, PostgreSQL",
                "abstract": "The personal portfolio website you are currently viewing, featuring dynamic content management.",
                "description": """
### Overview
A full-stack personal portfolio application designed to showcase projects, publications, and blogs.

**Key Features:**
- **Dynamic Content:** Custom Admin Dashboard for managing projects, certs, and blogs.
- **Modern UI:** Built with Vue 3 and TailwindCSS using a 'Cosmic' theme.
- **REST API:** Powered by Django REST Framework.
- **Deployment:** Dockerized and ready for cloud deployment.
                """,
                "repo_url": "https://github.com/tangiraiC/portifolio",
                "cover_image": "projects/my-portfolio/screenshot.png",
                "start_date": date(2024, 1, 15)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: My Portfolio'))

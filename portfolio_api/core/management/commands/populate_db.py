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
            ("AI and Machine Learning", "AI/ML Projects"),
            ("Business and Data Analytics", "Data Viz and Business Logic"),
            ("Hackathons", "Hackathon Projects"),
            ("Writing", "Blog posts and articles"),
        ]

        cat_objs = {}
        for name, desc in categories:
            cat, created = Category.objects.get_or_create(name=name, defaults={"description": desc})
            cat_objs[name] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Category: {name}'))
            else:
                self.stdout.write(f'Category already exists: {name}')

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
                "primary_category": cat_objs["Business and Data Analytics"],
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
                "primary_category": cat_objs["AI and Machine Learning"],
                "status": "completed",
                "tags_csv": "PyTorch, React, API",
                "tech_stack_csv": "Python, PyTorch, React, FastAPI",
                "abstract": "Deep learning model for classifying detailed image datasets with 98% accuracy.",
                "repo_url": "https://github.com/example/image-classifier",
                "start_date": date(2023, 11, 10)
            }
        )
        self.stdout.write(self.style.SUCCESS('Created/Updated Project: AI Image Classifier'))

        self.stdout.write(self.style.SUCCESS('Data population complete!'))

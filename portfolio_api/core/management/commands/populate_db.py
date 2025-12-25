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

        self.stdout.write(self.style.SUCCESS('Data population complete!'))

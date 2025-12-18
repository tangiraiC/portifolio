from core.models import Project, Category, BlogPost
from datetime import date

# Create Categories
web_dev, _ = Category.objects.get_or_create(name="Web Development", description="Web apps and sites")
ai_ml, _ = Category.objects.get_or_create(name="AI & Machine Learning", description="AI/ML Projects")
writing, _ = Category.objects.get_or_create(name="Writing", description="Blog posts and articles")

# Create Projects
p1, _ = Project.objects.get_or_create(
    title="E-Commerce Platform",
    defaults={
        "primary_category": web_dev,
        "status": "completed",
        "tags_csv": "Vue.js, Django, Postgres",
        "tech_stack_csv": "Vue.js, Python, PostgreSQL, Docker",
        "abstract": "A scalable e-commerce platform with real-time inventory management.",
        "repo_url": "https://github.com/example/ecommerce",
        "demo_url": "https://demo.example.com",
        "start_date": date(2024, 1, 15)
    }
)

p2, _ = Project.objects.get_or_create(
    title="AI Image Classifier",
    defaults={
        "primary_category": ai_ml,
        "status": "completed",
        "tags_csv": "PyTorch, React, API",
        "tech_stack_csv": "Python, PyTorch, React, FastAPI",
        "abstract": "Deep learning model for classifying detailed image datasets with 98% accuracy.",
        "repo_url": "https://github.com/example/image-classifier",
        "start_date": date(2023, 11, 10)
    }
)

# Create Sample Blog Posts
b1, _ = BlogPost.objects.get_or_create(
    title="The Future of AI in Web Dev",
    defaults={
        "slug": "future-ai-web-dev",
        "body_md": "AI is changing how we build websites. From coding assistants to automated testing...",
        "tags_csv": "AI, WebDev, Future",
        "published_at": date(2024, 3, 15)
    }
)

b2, _ = BlogPost.objects.get_or_create(
    title="Mastering Django Rest Framework",
    defaults={
        "slug": "mastering-drf",
        "body_md": "Django Rest Framework is a powerful toolkit for building Web APIs. In this guide...",
        "tags_csv": "Django, API, Python",
        "published_at": date(2024, 2, 20)
    }
)

print("Sample data created successfully!")

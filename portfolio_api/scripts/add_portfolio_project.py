from core.models import Project, Category
from datetime import date

def run():
    print("Starting to add 'My Portfolio' project...")

    # Get or create the category
    web_dev, _ = Category.objects.get_or_create(
        name="Web Development", 
        defaults={"description": "Web apps and sites"}
    )

    # Create or update the Project
    project, created = Project.objects.get_or_create(
        slug="my-portfolio",
        defaults={
            "title": "My Portfolio",
            "primary_category": web_dev,
            "status": "completed",
            "tags_csv": "Personal Brand, Full Stack, Interactive",
            "tech_stack_csv": "Django, Vue.js, TailwindCSS, PostgreSQL",
            "highlights_csv": "Custom Admin Dashboard\nModern UI with Cosmic theme\nDockerized deployment",
            "abstract": "The personal portfolio website you are currently viewing, featuring dynamic content management.",
            "description": """### Overview
A full-stack personal portfolio application designed to showcase projects, publications, and blogs.

**Key Features:**
- **Dynamic Content:** Custom Admin Dashboard for managing projects, certs, and blogs.
- **Modern UI:** Built with Vue 3 and TailwindCSS using a 'Cosmic' theme.
- **REST API:** Powered by Django REST Framework.
- **Deployment:** Dockerized and ready for cloud deployment.""",
            "repo_url": "", # User didn't provide one in the prompt snippet, can leave blank or placeholder
            "demo_url": "",
            "start_date": date.today(), # Or specific date if known
        }
    )

    if created:
        print(f"Successfully created project: {project.title}")
    else:
        print(f"Project '{project.title}' already exists. Updating details...")
        # Dictionary of fields to update
        updates = {
            "title": "My Portfolio",
            "primary_category": web_dev,
            "status": "completed",
            "tags_csv": "Personal Brand, Full Stack, Interactive",
            "tech_stack_csv": "Django, Vue.js, TailwindCSS, PostgreSQL",
            "highlights_csv": "Custom Admin Dashboard\nModern UI with Cosmic theme\nDockerized deployment",
            "abstract": "The personal portfolio website you are currently viewing, featuring dynamic content management.",
            "description": """### Overview
A full-stack personal portfolio application designed to showcase projects, publications, and blogs.

**Key Features:**
- **Dynamic Content:** Custom Admin Dashboard for managing projects, certs, and blogs.
- **Modern UI:** Built with Vue 3 and TailwindCSS using a 'Cosmic' theme.
- **REST API:** Powered by Django REST Framework.
- **Deployment:** Dockerized and ready for cloud deployment.""",
        }
        
        for key, value in updates.items():
            setattr(project, key, value)
        project.save()
        print(f"Successfully updated project: {project.title}")

if __name__ == "__main__":
    # verification trigger
    run()

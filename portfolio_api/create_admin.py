import os
import django
from django.contrib.auth import get_user_model

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_api.settings")
django.setup()

User = get_user_model()

def create_admin():
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    if not username or not password:
        print("Error: DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD must be set.")
        return

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser: {username}")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")
    else:
        print(f"Superuser '{username}' already exists. Skipping creation.")

if __name__ == "__main__":
    create_admin()

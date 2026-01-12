import os
import django
from django.contrib.auth import get_user_model

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_api.settings")
django.setup()

User = get_user_model()

def create_admin():
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "fibinacci")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "Lincoln@1122")

    if not username or not password:
        print("Error: DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD must be set.")
        return

    try:
        user = User.objects.get(username=username)
        print(f"Superuser '{username}' already exists. Updating password...")
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Password updated and permissions ensured.")
    except User.DoesNotExist:
        print(f"Creating superuser: {username}")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")

if __name__ == "__main__":
    create_admin()

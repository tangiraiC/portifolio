import os
import django
from django.utils import timezone
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_api.settings")
django.setup()

from core.models import Certification

def seed_certifications():
    certs = [
        {
            "name": "AWS Certified Solutions Architect",
            "issuing_organization": "Amazon Web Services",
            "issue_date": date(2025, 1, 15),
            "credential_url": "https://aws.amazon.com/verification",
            "credential_id": "AWS-123456"
        },
        {
            "name": "Google Data Analytics Professional Certificate",
            "issuing_organization": "Google",
            "issue_date": date(2024, 8, 20),
            "credential_url": "https://coursera.org/verify/google",
            "credential_id": "G-DATA-789"
        },
        {
            "name": "Certified Kubernetes Administrator",
            "issuing_organization": "CNCF",
            "issue_date": date(2024, 5, 10),
            "credential_url": "https://cncf.io/verify",
            "credential_id": "CKA-456"
        }
    ]

    for cert_data in certs:
        cert, created = Certification.objects.get_or_create(
            name=cert_data["name"],
            defaults=cert_data
        )
        if created:
            print(f"Created certification: {cert.name}")
        else:
            print(f"Certification already exists: {cert.name}")

if __name__ == "__main__":
    seed_certifications()

# core/filters.py
import django_filters as df
from .models import Project, Category
from django.db.models import Q


class ProjectFilter(df.FilterSet):

    # allow either category id or slug
    category = df.CharFilter(method="filter_category")
    status = df.CharFilter(field_name="status", lookup_expr="exact")
    tag = df.CharFilter(method="filter_tag")


    class Meta:
        model = Project
        fields = ["status"]


def filter_category(self, queryset, name, value):
    # if numeric, treat as id; else slug
    if value.isdigit():
        return queryset.filter(primary_category_id=int(value))
    return queryset.filter(primary_category__slug=value)


def filter_tag(self, queryset, name, value):
    # tags_csv is a comma‑separated string; case‑insensitive contains
    return queryset.filter(tags_csv__icontains=value)
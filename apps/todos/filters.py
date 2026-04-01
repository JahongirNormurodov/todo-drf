import django_filters

from apps.todos.models import Todo


class TodoFilter(django_filters.FilterSet):
    due_date_from = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="gte")
    due_date_to = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="lte")

    class Meta:
        model = Todo
        fields = ["status", "priority", "category", "folder", "label"]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.categories.views import CategoryViewSet
from apps.folders.views import FolderViewSet
from apps.labels.views import LabelViewSet
from apps.sub_todos.views import SubTodoViewSet
from apps.tags.views import TagViewSet
from apps.todos.views import TodoViewSet

router = DefaultRouter()
router.register(r"folders", FolderViewSet, basename="folder")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"todos", TodoViewSet, basename="todo")
router.register(r"tags", TagViewSet, basename="tag")
router.register(r"labels", LabelViewSet, basename="label")

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
    path(
        "folders/<uuid:folder_pk>/categories/",
        CategoryViewSet.as_view({"get": "list", "post": "create"}),
        name="folder-categories-list",
    ),
    path(
        "folders/<uuid:folder_pk>/categories/<uuid:pk>/",
        CategoryViewSet.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="folder-categories-detail",
    ),
    path(
        "categories/<uuid:category_pk>/todos/",
        TodoViewSet.as_view({"get": "list", "post": "create"}),
        name="category-todos-list",
    ),
    path(
        "categories/<uuid:category_pk>/todos/<uuid:pk>/",
        TodoViewSet.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="category-todos-detail",
    ),
    path(
        "todos/<uuid:todo_pk>/sub-todos/",
        SubTodoViewSet.as_view({"get": "list", "post": "create"}),
        name="todo-sub-todos-list",
    ),
    path(
        "todos/<uuid:todo_pk>/sub-todos/<uuid:pk>/",
        SubTodoViewSet.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="todo-sub-todos-detail",
    ),
]

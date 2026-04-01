from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from django.urls import path
from .views import RegisterView, MeView
from rest_framework_simplejwt.views import TokenObtainPairView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    *router.urls,
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('me/', MeView.as_view()),
]

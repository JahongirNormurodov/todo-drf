from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
## new imports
from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]

from .views import MeView

urlpatterns += [
    path('me/', MeView.as_view()),
]
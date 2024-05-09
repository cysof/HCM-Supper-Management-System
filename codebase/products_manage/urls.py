from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet

router = SimpleRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

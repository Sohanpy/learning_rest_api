from .views import ListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ListView, basename='articles')
urlpatterns = router.urls

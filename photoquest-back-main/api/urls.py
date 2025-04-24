from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    QuestViewSet,
    PublicSubmissionList,
    SubmissionViewSet,
    RegisterView,
    current_user,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Роутер для ViewSet'ов
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'quests', QuestViewSet, basename='quest')
router.register(r'submissions', SubmissionViewSet, basename='submission')

# Основные URL
urlpatterns = [
    path('', include(router.urls)),
    path('me/', current_user, name='current_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('photos/', PublicSubmissionList.as_view(), name='public-submissions'),
]

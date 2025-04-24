from rest_framework import viewsets
from .models import Category, Quest, Submission
from .serializers import CategorySerializer, QuestSerializer, SubmissionSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'role': request.user.role
    })


class IsAdminOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'moderator']

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        if self.request.user.role in ['admin', 'moderator']:
            return Submission.objects.all()
        return Submission.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # ⬅️ ВАЖНО!!!

    # ✅ Аппрув (утверждение)
    @action(detail=True, methods=['patch'], permission_classes=[IsAdminOrModerator])
    def approve(self, request, pk=None):
        submission = self.get_object()
        submission.status = 'approved'
        submission.save()
        return Response({'status': 'approved'}, status=status.HTTP_200_OK)

    # ❌ Отклонить (reject)
    @action(detail=True, methods=['patch'], permission_classes=[IsAdminOrModerator])
    def reject(self, request, pk=None):
        submission = self.get_object()
        submission.status = 'rejected'
        submission.save()
        return Response({'status': 'rejected'}, status=status.HTTP_200_OK)

    # ⭐ Выставить оценку
    @action(detail=True, methods=['patch'], permission_classes=[IsAdminOrModerator])
    def rate(self, request, pk=None):
        submission = self.get_object()
        rating = request.data.get('rating')

        if rating is None:
            return Response({'error': 'Rating is required!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                return Response({'error': 'Rating must be between 1 and 5!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'Rating must be an integer!'}, status=status.HTTP_400_BAD_REQUEST)

        submission.rating = rating
        submission.save()
        return Response({'status': 'rated', 'rating': rating}, status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from rest_framework import filters

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['difficulty']


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
from rest_framework.views import APIView
from .serializers import PublicSubmissionSerializer
from .models import Submission

class PublicSubmissionList(APIView):
    def get(self, request):
        submissions = Submission.objects.filter(status='approved')
        serializer = PublicSubmissionSerializer(submissions, many=True, context={'request': request})
        return Response(serializer.data)

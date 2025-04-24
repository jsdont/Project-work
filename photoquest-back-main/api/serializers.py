from rest_framework import serializers
from .models import Category, Quest, Submission
from django.contrib.auth import get_user_model
from .models import CustomUser  

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            role=validated_data.get('role', 'user')
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class QuestSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Показываем категорию красиво!
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Quest
        fields = ['id', 'title', 'description', 'difficulty', 'category', 'category_id']

class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # ⬅️ тут главное!
    
    class Meta:
        model = Submission
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
    
from rest_framework import serializers
from .models import Submission

class PublicSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'photo', 'comment', 'rating', 'created_at']
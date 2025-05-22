from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import AppSubmission

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")
        
        user = authenticate(request=self.context.get('request'), username=user.username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        
        attrs['user'] = user
        return attrs

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {'id': {'read_only': True}}

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.filter(email=value).exclude(id=user.id).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

class UserStatusSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password.')
            data['user'] = user
        else:
            raise serializers.ValidationError('Both email and password are required.')
        return data

class AppSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSubmission
        fields = ['id', 'app_image', 'app_name', 'app_link', 'app_category', 'subcategory', 'points', 'created_at']

    def validate(self, data):
        category = data.get('app_category')
        subcategory = data.get('subcategory')

        if category and subcategory:
            valid_subcategories = AppSubmission.SUBCATEGORIES.get(category, [])
            if subcategory not in valid_subcategories:
                raise serializers.ValidationError({
                    'subcategory': f"Invalid subcategory for category {category}. Valid options are: {', '.join(valid_subcategories)}"
                })
        return data
    


from rest_framework import serializers
from .models import ScreenshotSubmission, AppSubmission

class ScreenshotSubmissionSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    app_name = serializers.CharField(source='app_submission.app_name', read_only=True)
    points = serializers.IntegerField(source='app_submission.points', read_only=True)
    app_image = serializers.ImageField(source='app_submission.app_image', read_only=True)

    class Meta:
        model = ScreenshotSubmission
        fields = ['id', 'user', 'username', 'app_submission', 'app_name','app_image', 'points', 'app_screenshot', 'date']
        read_only_fields = ['id', 'user', 'username', 'app_name', 'points', 'date']
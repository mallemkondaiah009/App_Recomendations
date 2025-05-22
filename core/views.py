import logging
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ScreenshotSubmission, AppSubmission
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserListSerializer,
    ProfileSerializer,
    UserStatusSerializer,
    AppSubmissionSerializer,
    ScreenshotSubmissionSerializer,
)
from .permissions import AdminPostOnlyPermission

logger = logging.getLogger(__name__)

# API Views
class UserRegistrations(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = []  # Allow anyone to register

class UserLogin(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)  # Create session
            logger.info(f"User {user.username} logged in successfully")
            return Response({
                'status': 'success',
                'message': 'Login successful',
                'data': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                }
            }, status=200)
        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return Response({'status': 'error', 'detail': 'Failed to login'}, status=400)

class ListOfUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = []

class ListOfUsersWithPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'pk'
    permission_classes = []

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'pk'
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class UserStatusView(generics.CreateAPIView):
    serializer_class = UserStatusSerializer
    authentication_classes = [] 
    permission_classes = [AdminPostOnlyPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'is_staff': user.is_staff}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppSubmissionListCreateView(generics.ListCreateAPIView):
    queryset = AppSubmission.objects.all()
    serializer_class = AppSubmissionSerializer
    permission_classes = [AdminPostOnlyPermission]

class AppSubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppSubmission.objects.all()
    serializer_class = AppSubmissionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class ScreenshotSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ScreenshotSubmission.objects.all()
    serializer_class = ScreenshotSubmissionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user to the authenticated user
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ScreenshotSubmissionDetailView(generics.ListAPIView):
    queryset = ScreenshotSubmission.objects.all()
    serializer_class = ScreenshotSubmissionSerializer
    permission_classes = [IsAuthenticated]

# Template Views
class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class ProfileTemplateView(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)

class CustomAdminView(TemplateView):
    template_name = 'custom_admin.html'

def logout_view(request):
    logout(request)
    logger.info(f"User logged out")
    return redirect('/login/')

class UserTasksView(TemplateView):
    template_name = 'user_tasks.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)
    
class UserPointsView(TemplateView):
    template_name = 'user_points.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)

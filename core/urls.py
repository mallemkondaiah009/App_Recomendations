from django.urls import path
from .views import (
    UserRegistrations, UserLogin, ListOfUsers, ListOfUsersWithPk,
    ProfileView, RegisterView, LoginView, ProfileTemplateView, logout_view,
    AppSubmissionListCreateView, UserStatusView, CustomAdminView, AppSubmissionDetailView, HomeView,ScreenshotSubmissionViewSet,
    ScreenshotSubmissionDetailView,UserTasksView,UserPointsView
)

urlpatterns = [
    # API endpoints
    path('api/register/', UserRegistrations.as_view(), name='user-register'),
    path('api/login/', UserLogin.as_view(), name='user-login'),
    path('api/users/', ListOfUsers.as_view(), name='user-list'),
    path('api/users/<int:pk>/', ListOfUsersWithPk.as_view(), name='user-detail'),
    path('api/profile/<int:pk>/', ProfileView.as_view(), name='user-profile'),
    path('api/app_submissions/', AppSubmissionListCreateView.as_view(), name='app-submission-list-create'),
    path('api/app_submissions/<int:pk>/', AppSubmissionDetailView.as_view(), name='app-submission-detail'),
    path('api/user-status/', UserStatusView.as_view(), name='user-status'),
    path('api/screenshot-submissions/', ScreenshotSubmissionViewSet.as_view({'post': 'create'}), name='screenshot-submission-create'),
    path('api/tasks/', ScreenshotSubmissionDetailView.as_view(), name='screenshot-submission-list'),

    # Template endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileTemplateView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),
    path('custom_admin/', CustomAdminView.as_view(), name='custom-admin'),
    path('', HomeView.as_view(), name='home'),
    path('user_tasks/', UserTasksView.as_view(), name='user-tasks'),
    path('user_points/', UserPointsView.as_view(), name='user-points'),
]
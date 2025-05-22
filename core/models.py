# models.py
from django.db import models
from django.contrib.auth.models import User

class AppSubmission(models.Model):
    CATEGORIES = [
        ('Productivity', 'Productivity'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Social', 'Social'),
    ]
    
    SUBCATEGORIES = {
        'Productivity': ['Task Management', 'Note Taking', 'Time Tracking', 'Project Management', 'Collaboration Tools', 'Calendar Apps', 'Document Editing', 'Workflow Automation'],
        'Entertainment': ['Streaming', 'Gaming', 'Music', 'Video Editing', 'Live Events', 'Podcasts', 'Virtual Reality', 'Photo Editing'],
        'Education': ['Learning Platforms', 'Language Learning', 'Tutoring', 'Online Courses', 'Study Tools', 'Educational Games', 'Research Tools', 'Skill Development'],
        'Social': ['Messaging', 'Networking', 'Community', 'Social Media', 'Event Planning', 'Dating Apps', 'Forums', 'Content Sharing']
    }
    
    # Flat list of all subcategories for choices
    SUBCATEGORY_CHOICES = [
        (sub, sub) for category in SUBCATEGORIES.values() for sub in category
    ]

    app_image = models.ImageField(upload_to='app_images/', null=True, blank=True)
    app_name = models.CharField(max_length=255)
    app_link = models.URLField(max_length=200)
    app_category = models.CharField(max_length=50, choices=CATEGORIES)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_name


class ScreenshotSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    app_submission = models.ForeignKey(AppSubmission, on_delete=models.CASCADE)
    app_screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Screenshot for {self.app_submission.app_name} by {self.user.username}"

    class Meta:
        ordering = ['-date']


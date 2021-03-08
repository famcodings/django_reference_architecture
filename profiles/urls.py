from django.urls import path, include
from .views import DashBoardView, SignUpView, UpdateProfile

urlpatterns = [
    path('', DashBoardView.as_view(), name="dashboard"),
    path('', include("django.contrib.auth.urls")),
    path('signup', SignUpView.as_view(), name="signup"),
    path('profile', UpdateProfile.as_view(), name="profile"),
]

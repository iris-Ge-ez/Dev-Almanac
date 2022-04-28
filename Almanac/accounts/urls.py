from django.urls import path, include
from . import views

app_name = 'accounts_app'

urlpatterns = [
	path('user-registration/', views.UserRegistrationView.as_view(), name='user-registration'),
	path('user-list/', views.UserListView.as_view(), name='user-list'),
	path('user-profile/<str:username>/', views.UserProfileView.as_view(), name='user-detail'),
	path('user-profile-update/<str:username>/update/', views.UserProfileUpdateView.as_view(), name='user-update'),
]
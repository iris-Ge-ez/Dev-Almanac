from django.urls import path
from . import views

app_name = 'core_app'

urlpatterns = [
	path('project-post/', views.ProjectPostView.as_view(), name='project-post'),
	path('project-list/', views.ProjectListView.as_view(), name='project-list'),
	path('project-detail/<str:pid>/', views.ProjectDetailView.as_view(), name='project-detail'),
	path('project-update/<str:pid>/update/', views.ProjectUpdateView.as_view(), name='project-update'),

	path('hackathon-post/', views.HackathonPostView.as_view(), name='hackathon-post'),
	path('hackathon-list/', views.HackathonListView.as_view(), name='hackathon-list'),
	path('hackathon-detail/<str:hid>/', views.HackathonDetailView.as_view(), name='hackathon-detail'),
	path('hackathon-update/<str:hid>/update/', views.HackathonUpdateView.as_view(), name='hackathon-update'),

	path('task-post/', views.TaskPostView.as_view(), name='task-post'),
	path('task-list/', views.TaskListView.as_view(), name='task-list'),
	path('task-detail/<int:id>/', views.TaskDetailView.as_view(), name='task-detail'),
	path('task-update/<int:id>/update/', views.TaskUpdateView.as_view(), name='task-update'),

	path('application-post/', views.ApplicationPostView.as_view(), name='application-post'),
	path('application-list/', views.ApplicationListView.as_view(), name='application-list'),
	path('application-detail/<str:aid>/', views.ApplicationDetailView.as_view(), name='application-detail'),
	path('application-update/<str:aid>/update/', views.ApplicationUpdateView.as_view(), name='application-update'),

	path('enrollment-post/', views.EnrollmentPostView.as_view(), name='enrollment-post'),
	path('enrollment-list/', views.EnrollmentListView.as_view(), name='enrollment-list'),
	path('enrollment-detail/<str:eid>/', views.EnrollmentDetailView.as_view(), name='enrollment-detail'),
	path('enrollment-update/<str:eid>/update/', views.EnrollmentUpdateView.as_view(), name='enrollment-update'),
]
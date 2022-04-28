from django.contrib import admin
from core.models import Project, Hackathon, Task, Application, Enrollment, Prize

class ProjectAdminModel(admin.ModelAdmin):
	readonly_fields = ['pid']
	list_display = ('title', 'posted_by', 'posted_date', 'due_date')
	fieldsets = (
			('Project Detail', {
				'fields': ('title', 'description', 'tags', 'requirements', 'pid', 'posted_by', 'due_date')
				}),
		)

class HackathonAdminModel(admin.ModelAdmin):
	readonly_fields = ['hid']
	list_display = ('htitle', 'posted_by', 'go_live')
	fieldsets = (
			('Hackathon Detail', {
				'fields': ('title', 'description', 'tags', 'posted_by', 'go_live', 'hid', 'start_date_time', 'end_date_time')
				}),
		)

class TaskAdminModel(admin.ModelAdmin):
	list_display = ('hackathon', 'task_description')
	fieldsets = (
			('Task Detail', {
				'fields': ('hackathon', 'task_description')
				}),
		)

class ApplicationAdminModel(admin.ModelAdmin):
	readonly_fields = ['aid']
	list_display = ('user', 'project')
	fieldsets =(
			('Application Detail', {
				'fields': ('user', 'project', 'aid', 'attachement')
				}),
		)

class EnrollmentAdminModel(admin.ModelAdmin):
	readonly_fields = ['eid']
	list_display = ('user', 'hackathon')
	fieldsets = (
			('Enrollement Detail', {
				'fields': ('user', 'hackathon', 'eid')
				}),
		)

class PrizeAdminModel(admin.ModelAdmin):
    list_display = ('hackathon', 'prize_description')
    fieldsets = (
            ('Prize Detail', {
                'fields': ('hackathon', 'prize_description')
                }),
        )

admin.site.register(Project, ProjectAdminModel)
admin.site.register(Hackathon, HackathonAdminModel)
admin.site.register(Task, TaskAdminModel)
admin.site.register(Application, ApplicationAdminModel)
admin.site.register(Enrollment, EnrollmentAdminModel)
admin.site.register(Prize, PrizeAdminModel)
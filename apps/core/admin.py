from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.utils import quote
from django.contrib.admin.views.main import ChangeList

import apps.core.models 

# Register your models here.
for modelo in dir(apps.core.models):
	if getattr(apps.core.models, modelo).__class__.__name__== 'ModelBase' and getattr(apps.core.models, modelo).__class__.__name__ not in ['Encuentro','Club']:
		try:
			admin.site.register(getattr(apps.core.models, modelo))
		except:
			pass


class LogEntryAdmin(admin.ModelAdmin):
	readonly_fields=('content_type',
		'user',
		'action_time',
		'object_id',
		'object_repr',
		'action_flag',
		'change_message'
		)
	list_display=('action_flag','action_time','user','change_message','object_repr','object_id')

	def has_delete_permission(self,request,obj=None):
		return False

class CalendarioChageList(ChangeList):
	
	def url_for_result(self):
		return '/admin/core/calendario/'
	
	def get_model(self):
		return self.model.__name__

class CalendarioModelAdmin(admin.ModelAdmin):
	def get_changelist(self, request, **kwargs):
		return CalendarioChageList

admin.site.register(LogEntry,LogEntryAdmin)
# admin.site.register(apps.core.models.Encuentro, CalendarioModelAdmin)
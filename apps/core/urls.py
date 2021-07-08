from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.core.views import *
app_name='core'
urlpatterns=[
	
	path('calendario/', EncuentroCalendario.as_view(),name='encuentros_calendario'),
	path('api/encuentros/',EncuentroAPI.as_view(),name='api-encuentro'),

]
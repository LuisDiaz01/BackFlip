from django.urls import path, include
from apps.landing.views import Index, club_info
app_name='landing'
urlpatterns=[
	path('', Index.as_view(), name='index'),
	path('club', club_info, name='club_info'),
]
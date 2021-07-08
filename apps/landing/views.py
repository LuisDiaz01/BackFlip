from django.shortcuts import render
from apps.core.models import Post, Club
from django.views.generic import TemplateView
from apps.core.models import Club, Post
from django.http import JsonResponse
from pdb import set_trace
# Create your views here.


class Index(TemplateView):
	template_name="landing/index.html"

	def get(self, *args, **kwargs):
		# self.periodo = self.request.GET.get('periodo', settings.PERIODO_POR_DEFECTO)
		return super().get(*args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		data = super().get_context_data(*args, **kwargs)
		data['club'] = Club.objects.filter(pk=1)
		data['post'] = Post.objects.all().order_by('id')
		return data


def club_info(request):
	club=Club.objects.all().order_by('id')
	context={'club':club}
	return render(request, 'landing/club_info.html', context)

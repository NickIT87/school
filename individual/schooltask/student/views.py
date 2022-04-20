from django.views.generic import ListView
from django.shortcuts import render

from .models import Eleventh


# Create your views here.
class HomePageView(ListView):
    model = Eleventh
    template_name = "student/home.html"
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        return context

    def get_queryset(self):
        return Eleventh.objects.all()


class Search(ListView):
    template_name = 'student/searchResult.html'
    context_object_name = 'found_obj'

    def get_queryset(self):
        s = self.request.GET.get('s')
        return Eleventh.objects.filter(name__icontains=s)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "search"
        return context

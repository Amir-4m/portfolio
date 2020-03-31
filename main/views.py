#!/usr/bin/env python

from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from .models import Project, Skill
from .forms import MessageForm


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class HomePage(TemplateView, FormMixin):
    http_method_names = ['get', 'post']
    template_name = "main/index.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context.update({
            'projects': Project.objects.all(),
            'skills': Skill.objects.all()
        })
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('main:index')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.text = form.data['text']
        message.save()
        return super(HomePage, self).form_valid(form)

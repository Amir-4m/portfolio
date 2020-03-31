from django.contrib import admin
from .models import Project, Skill, Message


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'proficiency')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

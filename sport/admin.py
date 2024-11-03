from django.contrib import admin
from .models import Action , Course , Diet , Plan
# Register your models here.
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = list_display
    readonly_fields = ('created_date','update_date')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('teacher','student')
    list_display_links = list_display
    readonly_fields = ('created_date','update_date')

@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ('course','start_date','end_date')
    list_display_links = list_display
    readonly_fields = ('created_date','update_date')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('course','start_date','end_date','day_of_week')
    list_display_links = list_display
    readonly_fields = ('created_date','update_date')

from django.contrib import admin
from .models import Category, Quest, Submission

admin.site.register(Category)
admin.site.register(Quest)

from django.contrib import admin
from .models import Category, Quest, Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest', 'status', 'rating', 'created_at')
    list_filter = ('status', 'quest', 'created_at')
    search_fields = ('user__username', 'quest__title')

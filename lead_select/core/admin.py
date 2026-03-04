from django.contrib import admin
from .models import Election, Candidate

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'date_created')
    search_fields = ('title',)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'election')
    search_fields = ('name', 'election')


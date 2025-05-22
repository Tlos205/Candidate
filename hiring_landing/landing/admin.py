from django.contrib import admin
from .models import Candidate
# Register your models here.
@admin.register(Candidate)
class LandingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'description', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
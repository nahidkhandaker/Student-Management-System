from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'is_active', 'created_at')
    list_filter = ('course', 'is_active', 'created_at')
    search_fields = ('name', 'email', 'phone', 'course')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Academic Information', {
            'fields': ('course', 'is_active')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_inactive', 'mark_as_active']
    
    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(
            request,
            f"{updated} student{'s' if updated != 1 else ''} marked as inactive."
        )
    mark_as_inactive.short_description = "Mark selected students as inactive"
    
    def mark_as_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(
            request,
            f"{updated} student{'s' if updated != 1 else ''} marked as active."
        )
    mark_as_active.short_description = "Mark selected students as active"
    
    
    
from django.contrib import admin
from .models import About, Project, VisitorInfo


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_snippet', 'preview')
    readonly_fields = ('preview',)
    
    def preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100"/>'
        return "No Image"
    preview.allow_tags = True
    preview.short_description = 'Image Preview'

    def text_snippet(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_snippet.short_description = 'Text'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'url', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100"/>'
        return "No Image"
    preview.allow_tags = True
    preview.short_description = 'Image Preview'


@admin.register(VisitorInfo)
class VisitorInfoAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'mac_address', 'user_agent', 'timestamp')
    readonly_fields = ('ip_address', 'mac_address', 'user_agent', 'timestamp')

from django.contrib import admin
from django.utils.html import format_html
from .models import AboutMe, Project, ContactMessage


# ================= ABOUT ME =================
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "short_bio", "image_preview")
    readonly_fields = ("image_preview",)
    search_fields = ("name",)

    def short_bio(self, obj):
        return obj.bio[:60] + "..." if len(obj.bio) > 60 else obj.bio
    short_bio.short_description = "Bio"

    def image_preview(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="120" style="border-radius:8px;" />',
                obj.profile_picture.url
            )
        return "No Image"
    image_preview.short_description = "Profile Picture"


# ================= PROJECT =================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "language",
        "github_link",
        "project_preview",
    )
    list_filter = ("language",)
    search_fields = ("name", "description")
    readonly_fields = ("project_preview",)

    def project_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="150" style="border-radius:10px;" />',
                obj.image.url
            )
        return "No Image"
    project_preview.short_description = "Preview"


# ================= CONTACT MESSAGE =================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "is_sent_to_telegram",
        "created_at",
    )
    list_filter = ("is_sent_to_telegram", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")

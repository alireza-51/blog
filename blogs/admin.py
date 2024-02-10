from django.contrib import admin
from .models import Post, Tag, Comment

admin.site.register([Tag, Comment])

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "slug",
    )
    # list_filter = (
    #     "published",
    #     "publish_date",
    # )
    list_editable = (
        "title",
        "slug",
    )
    search_fields = (
        "title",
        "slug",
        "content",
    )
    prepopulated_fields = {
        "slug": (
            "title",
        )
    }
    date_hierarchy = "updated"
    save_on_top = True
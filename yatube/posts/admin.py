from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text", "group", "pub_date",)
    search_fields = ("text",)
    list_filter = ("author", "pub_date")
    list_editable = ('group',)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Group)

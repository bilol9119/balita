from django.contrib import admin
from .models import Post, Tags, BioPost, Comment, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'id', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BioPostAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagAdmin)
admin.site.register(BioPost, BioPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
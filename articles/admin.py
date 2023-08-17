from django.contrib import admin
from articles.models import Article, Comment


# Register your models here.


# class CommentInline(admin.StackedInline):  # new
#     model = Comment
#     extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

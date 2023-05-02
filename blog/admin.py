from django.contrib import admin
from django.forms import Textarea
from django.db import models

from blog.models import PostCategory, Post, Comment, Redactor


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'published',
        'created_at',
        'redactor',
        'illustration',
        'comments_count',
    )

    list_filter = (
        'category__name',
        'published',
    )

    # Selection automatique en saisissant du contenu
    autocomplete_fields = ['category']
    # changer le widget de la zone de saisie d'un post dans l'interface admin.
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})}}

    def comments_count(self, obj):
        '''
        :param obj:
        :return: number of comments for a post
        '''
        return Comment.objects.filter(post=obj).count()

    # Libellé dans l'interface d'admin
    comments_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = [
        'post__title',
        'author_name',
    ]

    list_display = (
        'post',
        'author_name',
        'status',
        'created_at',
        'moderation_text',
        'text',
    )

    list_filter = (
        'status',
                   )

    list_editable = (
        'status',
        'moderation_text',
    )

@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
    )

    list_filter = (
        'first_name',
        'last_name',
    )
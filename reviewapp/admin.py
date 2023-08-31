from django.contrib import admin
from .models import CarReviewModel, CarCommentModel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CarReviewModel)           # adding a decorator
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('formula_name', 'slug', 'status', 'created_on')
    search_fields = ['formula_name', 'content',]
    prepopulated_fileds = {'slug': ('formula_name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(CarCommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'created_on', 'approved_by_admin')
    list_filter = ('approved_by_admin', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approve=True)

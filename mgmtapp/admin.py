from django.contrib import admin
from models import *

# Register your models here.


class DiscussionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Discussion Details', {'fields': ('added_by','creater_id','title','text','discussion_type','is_published','image',)}),
    )


    ordering = ('-created_date',)
    list_display = ('title','text','discussion_type',)
    search_fields = ('title','text',)
    list_filter = ('is_published','discussion_type', )

class CommentAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Comment Details', {'fields': ('discussion','text','added_by')}),
    )


    ordering = ('-created_date',)
    list_display = ('discussion','text','added_by')
    search_fields = ('discussion','text',)
    

admin.site.register(Comment,CommentAdmin)
admin.site.register(Discussion,DiscussionAdmin)
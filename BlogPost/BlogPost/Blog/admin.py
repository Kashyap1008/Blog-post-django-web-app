from django.contrib import admin

# Register your models here.

from .models import Post





@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','date_posted','author','title_length')

    list_filter = ('title','author','date_posted')

    search_fields = ('title','body')

    ordering = ('-date_posted',)

    list_per_page = 20

    #list_editable = ('published') // currently this field does not exists

    fieldsets = (
        (
            'Post information',{'fields': ('title','content')}
        ),
        (
            'Metadata',{'fields': ('author','date_posted')}
        )
    )
    
    readonly_fields = ('date_posted',)

    date_hierarchy = ('date_posted')

    #we dont have publish so we are not making admin action

admin.site.site_header = ('Blog Administration')
admin.site.site_title = ('Blog Admin')
admin.site.index_title = ('welcome to blog admin')
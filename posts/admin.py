from django.contrib import admin
from .models import Article


# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # fields = ['title','auther','created','edited']
    readonly_fields = ['created','edited','slug']
    fieldsets = (
        (None,{
            "fields" : ('title', 'auther','slug','image')
        }),
        ('Important dates',{
            "fields" : ('created','edited')
        }),
        ('Content',{
            "fields" : ['content',"status"]
        }),
    )
    list_display = ['title','auther','status','created','edited']
    list_filter = ['status','created']
    search_fields = ("title","auther __username")


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title','auther','status','created','edited']
#     list_filter = ['status','created']
#     search_fields = ("title","auther __username")
# admin.site.register(Article,ArticleAdmin)
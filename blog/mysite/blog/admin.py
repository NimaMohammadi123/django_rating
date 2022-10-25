from django.contrib import admin
from .models import Post ,Rating
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','publish','status','rating','slug')
    list_filter = ('status',)
    search_fields = ('title','body')
    list_editable = ('status',)
    
admin.site.register(Rating)
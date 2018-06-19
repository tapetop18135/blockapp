from django.contrib import admin
from .models import Blocktable
# Register your models here.
@admin.register(Blocktable)
class Blocktable(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id', 'title', 'content', 'authId', 'date',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
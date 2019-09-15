from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


admin.site.register(Post, NewsAdmin)
admin.site.register(Review, NewsAdmin)

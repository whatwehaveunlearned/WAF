from django.contrib import admin
from .models import English, Chinese, Spanish, WafUser, Languages

class VocabAdmin(admin.ModelAdmin):
	list_display = ('word','definition','definition','tags','image','sound','created','modified')
	search_fields = ('word','definition','tags','created','modified')
	list_filter = ('word','definition','tags','created','modified')
	ordering = ('-word',)

admin.site.register(English, VocabAdmin)
admin.site.register(Spanish, VocabAdmin)
admin.site.register(Chinese, VocabAdmin)
admin.site.register(WafUser)
admin.site.register(Languages)

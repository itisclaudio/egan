from django.contrib import admin
from parse.parseapp.models import (
	Methodologies, 
	)


class MethodologiesAdmin(admin.ModelAdmin):
	list_display = ['id','title','dateadded']
		
admin.site.register(Methodologies, MethodologiesAdmin)
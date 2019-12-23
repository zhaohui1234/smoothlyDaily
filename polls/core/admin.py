from django.contrib import admin

# Register your models here.

from .models import Staff, Job, Record

admin.site.register(Staff)
admin.site.register(Job)
admin.site.register(Record)

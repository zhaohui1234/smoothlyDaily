from django.contrib import admin
from .models import User , Activity
# Register your models here.

#admin.site.register(User)
#admin.site.register(Activity)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'wx_name', 'create_time')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display=('id', 'user_id' , 'seq' ,  'create_time', 'end_time' ,'state')






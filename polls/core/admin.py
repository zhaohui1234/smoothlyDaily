from django.contrib import admin

from core.models import Staff, Job, Record

# Register your models here.

##from .models import Staff, Job, Record
##
##admin.site.register(Staff)
##admin.site.register(Job)
##admin.site.register(Record)

  
#staff模型的管理器
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'description')


#Job模型的管理器
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=('id', 'name')


#staff模型的管理器
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display=('id', 'staff', 'job', 'date')


    def sendJson(self):
        print("YES  ******************* send !!!!!")

    def save_model(self, request, obj, form, change):
        #trigger the websocket
        self.sendJson()
        
        super().save_model(request, obj, form, change)

   

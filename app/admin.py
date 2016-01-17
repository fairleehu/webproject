from django.contrib import admin
from app.models import *

# Register your models here.


class AtSendAdmin(admin.ModelAdmin):
    list_display = ('sendType', 'sendText', 'sendTime', 'sendDept')


class AtUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'userDept', 'userJob', 'userImage')


class AtLeaveAdmin(admin.ModelAdmin):
    list_display = ('leaveName', 'leaveType', 'leaveDate', 'leaveFDate','leaveText')
admin.site.register(AtUser, AtUserAdmin)
admin.site.register(Dept)
admin.site.register(AtSend, AtSendAdmin)
admin.site.register(AtLeave, AtLeaveAdmin)

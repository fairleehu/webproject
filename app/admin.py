from django.contrib import admin
from app.models import *

# Register your models here.


class AtSendAdmin(admin.ModelAdmin):
    list_display = ('sendType', 'sendText', 'sendTime', 'sendDept')


class AtUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'userDept', 'userJob', 'userImage')

    def save_model(self, request, obj, form, change):
        if obj.add_user == u'':
            obj.add_user = request.user.userDept
        obj.last_edit_user = request.user.userDept
        obj.save()


admin.site.register(AtUser, AtUserAdmin)
admin.site.register(Dept)
admin.site.register(AtSend, AtSendAdmin)

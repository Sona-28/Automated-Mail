from django.contrib import admin
from .models import Mail, Upld, Att, Temp

admin.site.register(Mail)
admin.site.register(Temp)
admin.site.register(Upld)
admin.site.register(Att)

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CodeSkill)
admin.site.register(DesignSkill)
admin.site.register(Knowledge)
admin.site.register(Education)
admin.site.register(Experience)
from django.contrib import admin
from core.models import *

# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameters','updated_date','created_date']
    search_fields = ['name','description','parameters']
    list_editable = ['description','parameters']
    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','file','updated_date','created_date']
    search_fields = ['name','description','file']
    list_editable = ['description','file']
    class Meta:
        model = ImageSetting

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','order','name','percentage','updated_date','created_date']
    search_fields = ['name']
    list_editable = ['order','name','percentage']
    class Meta:
        model = Skill
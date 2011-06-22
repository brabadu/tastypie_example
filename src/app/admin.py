from django.contrib import admin

from app.models import Cabinet, Folder, File, FileType

admin.site.register(Cabinet)
admin.site.register(Folder)
admin.site.register(File)
admin.site.register(FileType)

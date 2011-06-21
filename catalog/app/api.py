from tastypie.resources import ModelResource
from tastypie import fields

from app.models import Cabinet, Folder, File


class FileResource(ModelResource):
    class Meta:
        queryset = File.objects.all()
        excludes = ['id']
        include_resource_uri = False


class FolderResource(ModelResource):
    files = fields.ToManyField('app.api.FileResource', 'files', full=True)

    class Meta:
        queryset = Folder.objects.all()
        excludes = ['id']
        include_resource_uri = False


class CabinetResource(ModelResource):
    folders = fields.ToManyField('app.api.FolderResource', 'folders', full=True)

    class Meta:
        queryset = Cabinet.objects.all()
        resource_name = 'cabinet/list'
        excludes = ['id']
        include_resource_uri = False

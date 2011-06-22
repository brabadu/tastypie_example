from tastypie.resources import ModelResource
from tastypie import fields

from app.models import Cabinet, Folder, File, FileType


class FileTypeResource(ModelResource):
    class Meta:
        queryset = FileType.objects.all()

    def dehydrate(self, bundle):
        return bundle.data['type']


class FileResource(ModelResource):
    type = fields.ToOneField('app.api.FileTypeResource', 'type', full=True)

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

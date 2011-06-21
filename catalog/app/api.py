from tastypie.resources import ModelResource
from tastypie import fields

from app.models import Cabinet, Folder


class FolderResource(ModelResource):
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

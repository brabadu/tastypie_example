from tastypie.resources import ModelResource

from app.models import Cabinet


class CabinetResource(ModelResource):
    class Meta:
        queryset = Cabinet.objects.all()

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Saglik


class SaglikSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Saglik
        geo_field = 'POINT'
        fields = '__all__'
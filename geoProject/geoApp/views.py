from .serializers import SaglikSerializer
from rest_framework import viewsets
from .models import Saglik



class SaglikViewSet(viewsets.ModelViewSet):
    queryset         = Saglik.objects.all()
    serializer_class = SaglikSerializer
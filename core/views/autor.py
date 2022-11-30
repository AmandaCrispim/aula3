from rest_framework.viewsets import ModelViewSet

from core.serializers import AutorSerializer
from core.models import Autor


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

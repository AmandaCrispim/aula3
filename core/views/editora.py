from rest_framework.viewsets import ModelViewSet

from core.serializers import EditoraSerializer
from core.models import Editora


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

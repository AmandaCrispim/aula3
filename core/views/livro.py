from rest_framework.viewsets import ModelViewSet

from core.serializers import LivroSerializer
from core.models import Livro


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

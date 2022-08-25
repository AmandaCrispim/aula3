from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora, Autor, Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all___"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all___"


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all___"


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all___"

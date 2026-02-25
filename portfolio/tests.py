from django.test import TestCase
from django.contrib.auth.models import User
from .models import Professor, Curso, Postagem

class ModelsTestCase(TestCase):
    def setUp(self):
        self.professor = Professor.objects.create(
            nome="Ana Souza",
            email="ana@teste.com",
            materia="Matemática"
        )
        self.curso = Curso.objects.create(
            nome="Álgebra Linear",
            carga_horaria=60,
            professor=self.professor
        )
        self.usuario = User.objects.create_user(
            username="joao", password="123456"
        )
        self.postagem = Postagem.objects.create(
            titulo="Primeira Aula",
            conteudo="Conteúdo da primeira aula",
            autor=self.usuario
        )

    def test_professor_str(self):
        self.assertEqual(str(self.professor), "Ana Souza")

    def test_curso_str(self):
        self.assertEqual(str(self.curso), "Álgebra Linear")

    def test_postagem_str(self):
        self.assertEqual(str(self.postagem), "Primeira Aula")

    def test_relacao_curso_professor(self):
        self.assertEqual(self.curso.professor, self.professor)

    def test_relacao_postagem_autor(self):
        self.assertEqual(self.postagem.autor.username, "joao")

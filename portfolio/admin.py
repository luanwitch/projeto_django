from django.contrib import admin
from .models import Professor, Curso, Postagem

# Admin para Professor
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'materia')

# Admin para Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'professor')

# Admin para Postagem
@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    fields = ('titulo', 'conteudo')  # autor será preenchido automaticamente

    # Define autor automaticamente ao criar a postagem
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # somente ao criar
            obj.autor = request.user
        super().save_model(request, obj, form, change)

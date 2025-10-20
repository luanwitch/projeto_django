from django.contrib import admin
from .models import Professor, Curso, Postagem


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'materia')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'professor')


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    readonly_fields = ('data_publicacao',)
    # Removemos o 'exclude', vamos tratar o campo manualmente

    def get_fields(self, request, obj=None):
        """
        Define os campos que aparecem no formulário.
        O campo 'autor' só aparece se o usuário for superuser.
        """
        fields = ['titulo', 'conteudo']
        if request.user.is_superuser:
            fields.append('autor')
        return fields

    def save_model(self, request, obj, form, change):
        """
        Define o autor automaticamente ao criar nova postagem.
        """
        if not obj.pk or not obj.autor_id:
            obj.autor = request.user
        super().save_model(request, obj, form, change)

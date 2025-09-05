from django.contrib import admin
from .models import Professor, Curso, Postagem

admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Postagem)
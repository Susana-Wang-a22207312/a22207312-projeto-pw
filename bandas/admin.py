from django.contrib import admin
from .models import Banda, Album, Musica, Membro, Comentario

admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Musica)
admin.site.register(Membro)
admin.site.register(Comentario)

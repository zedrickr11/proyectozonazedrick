from django.contrib import admin
from discografica.models import Genero, Artista, Album, Vocalista, Cancion, VocalistaAdmin, CancionAdmin
# Register your models here.
admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Album)
admin.site.register(Vocalista, VocalistaAdmin)
admin.site.register(Cancion, CancionAdmin)

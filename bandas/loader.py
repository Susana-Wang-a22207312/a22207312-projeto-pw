import json
from bandas.models import Banda, Album, Musica, Membro, Comentario

with open('bandas/json/primeiro.json') as f:
    data = json.load(f)

for item in data:
    model_name = item['model']
    if model_name == 'bandas.banda':
        fields = item['fields']
        banda = Banda.objects.create(
            nome=fields['nome'],
            genero=fields['genero'],
            ano_formacao=fields['ano_formacao'],
            pais_origem=fields['pais_origem']
        )
    elif model_name == 'bandas.album':
        fields = item['fields']
        banda = Banda.objects.get(pk=fields['banda'])
        album = Album.objects.create(
            titulo=fields['titulo'],
            banda=banda,
            gravadora=fields['gravadora'],
            capa_album=fields['capa_album']
        )
    elif model_name == 'bandas.musica':
        fields = item['fields']
        album = Album.objects.get(pk=fields['album'])
        musica = Musica.objects.create(
            titulo=fields['titulo'],
            album=album,
            duracao=fields['duracao'],
            numero_faixa=fields['numero_faixa']
        )
    elif model_name == 'bandas.membro':
        fields = item['fields']
        banda = Banda.objects.get(pk=fields['banda'])
        membro = Membro.objects.create(
            nome=fields['nome'],
            banda=banda,
            papel_na_banda=fields['papel_na_banda']
        )
    elif model_name == 'bandas.comentario':
        fields = item['fields']
        album = Album.objects.get(pk=fields['album'])
        comentario = Comentario.objects.create(
            autor=fields['autor'],
            texto=fields['texto'],
            album=album
        )

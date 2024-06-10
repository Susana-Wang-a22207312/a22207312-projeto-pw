from lusofona.models import Curso, Disciplina, Projeto, AreaCientifica
import json

def importar_curso(ficheiro_json):
    with open('lusofona/json/lei.json') as f:
        data = json.load(f)

    curso, created = Curso.objects.get_or_create(id=1)
    curso.apresentacao = data.get('apresentacao')
    curso.objetivos = data.get('objetivos')
    curso.competencias = data.get('competencias')
    curso.save()

    for disciplina_data in data.get('disciplinas', []):
        area_cientifica_nome = disciplina_data.get('area_cientifica')
        area_cientifica, created = AreaCientifica.objects.get_or_create(nome=area_cientifica_nome)

        disciplina, created = Disciplina.objects.get_or_create(
            nome=disciplina_data.get('nome'),
            ano=disciplina_data.get('ano'),
            semestre=disciplina_data.get('semestre'),
            ects=disciplina_data.get('ects'),
            curricularUnitReadableCode=disciplina_data.get('curricularUnitReadableCode'),
            area_cientifica=area_cientifica
        )

        projeto_data = disciplina_data.get('projeto', {})
        projeto, created = Projeto.objects.get_or_create(
            descricao=projeto_data.get('descricao'),
            conceitos_aplicados=projeto_data.get('conceitos_aplicados'),
            tecnologias_usadas=projeto_data.get('tecnologias_usadas'),
            video_demo=projeto_data.get('video_demo'),
            github_repo=projeto_data.get('github_repo'),
            disciplina=disciplina
        )

    print("Importação concluída.")

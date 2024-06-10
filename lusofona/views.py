from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Disciplina, Projeto, Docente
from .forms import DisciplinaForm, ProjetoForm, DocenteForm

def index_view(request):
    context = {
        'disciplinas': Disciplina.objects.all().order_by('nome'),
    }
    return render(request, "curso/index.html", context)

def disciplina_view(request, disciplina_id):
    context = {
      'disciplina': Disciplina.objects.get(id=disciplina_id),
   }
    return render(request, "curso/disciplina.html", context)

def projeto_view(request, projeto_id):
    context = {
      'projeto': Projeto.objects.get(id=projeto_id),
   }
    return render(request, "curso/projeto.html", context)

def docente_view(request, docente_id):
    context = {
      'docente': Docente.objects.get(id=docente_id),
   }
    return render(request, "curso/docente.html", context)

@login_required
def nova_disciplina_view(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_view')
    return render(request, 'curso/nova_disciplina.html', {'form': form})

@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('disciplina_view', disciplina_id=disciplina.id)
    return render(request, 'curso/edita_disciplina.html', {'form': form, 'disciplina': disciplina})

@login_required
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('index_view')
    return render(request, 'curso/apaga_disciplina.html', {'disciplina': disciplina})

@login_required
def novo_projeto_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.disciplina = disciplina
            projeto.save()
            return redirect('cursos:disciplina', disciplina_id=disciplina.id)
    else:
        form = ProjetoForm()

    return render(request, 'curso/novo_projeto.html', {'form': form, 'disciplina': disciplina})


@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projeto_view', projeto_id=projeto.id)
    return render(request, 'curso/edita_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('index_view')
    return render(request, 'curso/apaga_projeto.html', {'projeto': projeto})

@login_required
def novo_docente_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            docente = form.save()
            disciplina.docente = docente
            disciplina.save()
            return redirect('cursos:disciplina', disciplina_id=disciplina.id)
    else:
        form = DocenteForm()

    return render(request, 'curso/novo_docente.html', {'form': form, 'disciplina': disciplina})

@login_required
def edita_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    form = DocenteForm(request.POST or None, instance=docente)
    if form.is_valid():
        form.save()
        return redirect('docente_view', docente_id=docente.id)
    return render(request, 'curso/edita_docente.html', {'form': form, 'docente': docente})

@login_required
def apaga_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    if request.method == 'POST':
        docente.delete()
        return redirect('index_view')
    return render(request, 'curso/apaga_docente.html', {'docente': docente})
from .models import Tarefa
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect

# Por padrão a listview vai procurar nomeApp_list
class TarefaListView(ListView):
    model = Tarefa

class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ["titulo", "dt_prevista"]
    success_url = reverse_lazy("tarefas-list")

class TarefaUpdateView(UpdateView):
   model = Tarefa
   fields = ["titulo", "dt_prevista"]
   success_url = reverse_lazy("tarefas-list")

class TarefaDeleteView(DeleteView):
   model = Tarefa
   success_url = reverse_lazy("tarefas-list")


class TarefaCompleteView(View):
     def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.mark_has_complete()
        return redirect("tarefas-list")


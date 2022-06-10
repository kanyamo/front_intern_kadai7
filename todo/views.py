from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Todo
from .forms import TodoForm

class IndexCreateView(CreateView):
    form_class = TodoForm
    success_url = reverse_lazy("todo:index")


class IndexListView(ListView):
    model = Todo
    paginate_by = 10

    def get_queryset(self):
        return Todo.objects.order_by("deadline_date", "deadline_time")


class IndexView(IndexCreateView, IndexListView):
    template_name = "todo/index.html"


def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todo:index")
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDo
from .forms import FormTodo


def home(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = FormTodo(request.POST)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            ToDo.objects.get(pk=pk).delete()
        elif 'toggle' in request.POST:
            pk = request.POST.get('toggle')
            tarea = ToDo.objects.get(pk=pk)
            tarea.complete = not tarea.complete
            tarea.save()
        return HttpResponseRedirect(request.path_info)

    tareas = ToDo.objects.all()
    form = FormTodo()
    return render(request, 'home.html', {'tareas': tareas, 'form': form})

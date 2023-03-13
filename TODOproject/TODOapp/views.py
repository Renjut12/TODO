from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here

# ..........views creations based on class.............

class TaskListView(ListView):
    model = Task
    template_name = 'Home.html'
    contex_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('TODOapp:cbvdetail',kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'Delete.html'
    success_url = reverse_lazy('TODOapp:cbvHome')





















# ..........views creations based on functions.............

def Home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')

        task = Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'Home.html',{'task1':task1})

def Details(request):

    return render(request,'Details.html',)


def Delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request,'Delete.html')


def update(request,id):
    life = Task.objects.get(id=id)
    full = TodoForm(request.POST or None,instance=life)
    if full.is_valid():
        full.save()
        return redirect('/')

    return render(request,'edit.html',{'full':full,'life':life})



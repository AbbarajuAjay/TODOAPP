from django.shortcuts import render, redirect
from .models import TaskModel
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'activities/register.html', {'form': form})

class PostListView(ListView):
    model = TaskModel
    template_name = 'activities/viewall.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tasks'
    ordering = ['-created']

class PostUpdateView(UpdateView):
    model = TaskModel
    template_name = 'activities/update.html'
    fields = ['title', 'complete']
    success_url = reverse_lazy('viewall-view') 

class PostCreateView(CreateView):
    model = TaskModel
    template_name = 'activities/create.html'
    fields = ['title', 'complete']
    success_url = reverse_lazy('viewall-view')

class PostDeleteView(DeleteView):
    model = TaskModel
    template_name = 'activities/delete.html'
    success_url = reverse_lazy('viewall-view')




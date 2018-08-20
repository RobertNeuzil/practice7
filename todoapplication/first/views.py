from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import ToDo
from .forms import ToDoForm


def index(request):
	todolist = ToDo.objects.order_by('id')
	
	form = ToDoForm()

	context = {'todolist': todolist, 'form': form}
	


	return render(request, 'first/index.html', context)

@require_POST
def addtodo(request):

	form = ToDoForm(request.POST)

	


	if form.is_valid():
		new_todo = ToDo(text=request.POST[
		'text'])
		new_todo.save()



	return redirect('index')

# Create your views here.

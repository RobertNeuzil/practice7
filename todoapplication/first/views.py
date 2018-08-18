from django.shortcuts import render
from .models import ToDo
from .forms import ToDoForm


def index(request):
	todolist = ToDo.objects.order_by('id')
	
	form = ToDoForm()

	context = {'todolist': todolist, 'form': form}
	


	return render(request, 'first/index.html', context)

# Create your views here.

from django.shortcuts import render
from .models import ToDo

def index(request):
	todolist = ToDo.objects.order_by('id')
	context = {'todolist': todolist}
	return render(request, 'first/index.html', context)

# Create your views here.

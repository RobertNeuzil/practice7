from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


from .models import Todo
from .forms import Todoform


# Create your views here.

def index(request):
	to_do_list = Todo.objects.order_by("id")

	form = Todoform()
	
	context = { "to_do_list" : to_do_list, "form": form }



	return render(request, "todo/index.html", context)

@require_POST
def addtodo(request):
	form = Todoform(request.POST)
	print (request.POST['text'])
	return redirect('index')
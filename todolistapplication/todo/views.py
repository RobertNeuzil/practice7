from django.shortcuts import render

from .models import Todo
from .forms import Todoform


# Create your views here.

def index(request):
	to_do_list = Todo.objects.order_by("id")

	form = Todoform()
	
	context = { "to_do_list" : to_do_list, "form": form }



	return render(request, "todo/index.html", context)


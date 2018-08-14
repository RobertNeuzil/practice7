from django.shortcuts import render

from .models import Todo


# Create your views here.

def index(request):
	to_do_list = Todo.objects.order_by("id")
	context = { "to_do_list" : to_do_list }
	return render(request, "todo/index.html", context)
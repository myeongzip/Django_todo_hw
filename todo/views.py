from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo



# Create your views here.

def todo_index(request):
    pass


@csrf_exempt
def todo_create(request):
    if request.method == "POST":
        Todo.objects.create(
        content = request.POST['content'],
        user = request.user,
        is_done = request.POST.get('is_done', False),   # update에 써야겠다
        image = request.FILES.get('image')
        )
        return redirect('/todo/')
    elif request.method == "GET":
        return render(request, 'todo/create.html')
    else:
        return HttpResponse("Invalid request method", status=405)


def todo_read(request):
    pass
    
def todo_update(request):
    pass
def todo_delete(request):
    pass
    
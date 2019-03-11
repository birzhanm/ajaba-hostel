from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Block

# Create your views here.
def block_list(request):
    blocks = Block.objects.all()
    context = {'blocks':blocks}
    return render(request, 'rooms/block_list.html',context)

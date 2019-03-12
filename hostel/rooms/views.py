from django.shortcuts import render, get_object_or_404
from .models import Block

# Create your views here.
def block_list(request):
    blocks = Block.objects.all()
    context = {'blocks':blocks}
    return render(request, 'rooms/block_list.html', context)

def block_detail(request, pk):
    current_block = get_object_or_404(Block, pk=pk)
    rooms = current_block.room_set.all()
    context = {'current_block': current_block, 'rooms':rooms}
    return render(request, 'rooms/block_detail.html', context)

from django.shortcuts import render
from .forms import CheckinForm
from rooms.models import Room


def checkin(request, pk):
    if request.method == "POST":
        form = CheckinForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tenant = request.user.tenant
            booking.room = Room.objects.get(pk=pk)
            booking.save()
            return redirect('rooms:block_list')
    else:
        form = CheckinForm()
    context = {'form':form}
    return render(request, 'bookings/checkin.html', context)

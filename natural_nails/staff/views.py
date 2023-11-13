from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff

# Create your views here.
def staff(request):
    myStaffs = Staff.objects.all().values()
    context = {"staffs": myStaffs}
    return render(request, 'staff.html', context)

def staff_add(request):
    return render(request, 'staff_add_update.html')

def staff_update(request, id):
    myStaffs = Staff.objects.all()
    chosenStaff = next((s for s in myStaffs if s.id == id), None)
    return render(request, 'staff_add_update.html', chosenStaff)



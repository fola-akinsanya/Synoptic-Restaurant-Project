from django.shortcuts import render, redirect

from booking.forms import BookingForm

# Create your views here.
def booking(request):

    if request.method == "POST":
        booking_form = BookingForm(request.POST, customer= request.user)

        if booking_form.is_valid():

            booking_form.save()
            return redirect("booking-requested")

    else:
        context = {
        'booking_form': BookingForm(),
        }
        
        return render (request, "booking.html", context)

def booking_requested(request):
	if request.method == "GET":
		return render (request, "booking_requested.html")

def active_order_exists(request):
	if request.method == "GET":
		return render (request, "active_order_exists.html")
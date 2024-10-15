from django.shortcuts import render
# Create your views here.
def trangphim_view(request):
    return render(request,"trangphim.html")
def bookticket_view(request):
    return render (request, "bookticket.html")
def comboselection_view(request):
    return render(request, "comboselection.html")
def checkout_view(request):
    return render (request,"checkout.html")

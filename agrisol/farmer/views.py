from django.shortcuts import render

# Create your views here.
def farmer(request):
    return render(request,'farmer/farmer.html')
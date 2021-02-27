from django.shortcuts import render

# Create your views here.
from .models import Send


# def send_en(request):
#     sent = Send.objects.first()
#     context = {
#         'sent': sent
#     }
#     return render(request,'sent.html',s)
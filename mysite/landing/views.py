from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kvargs):
        return render(request, 'landing/index.html')
        


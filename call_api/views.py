from django.shortcuts import render

# Create your views here.
def call_api_page(request):
    
    return render(request,'call_api/index.html')

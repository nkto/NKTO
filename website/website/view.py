from django.shortcuts import render

def index(request):
    return render(request, 'nktoindex.html')

def admin(request):
    return render(request, 'admin.html')

def productdetail(request):
    return render(request, 'productdetail.html')
  
def signin(request):
    return render(request, 'signin.html')

def setting(request):
    return render(request, 'setting.html')
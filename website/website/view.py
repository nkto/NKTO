from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    return render(request, 'nktoindex.html')

@ensure_csrf_cookie
def admin(request):
    return render(request, 'admin.html')

@ensure_csrf_cookie
def productdetail(request):
    return render(request, 'nktoproductdetail.html')

@ensure_csrf_cookie
def signin(request):
    return render(request, 'signin.html')

@ensure_csrf_cookie
def setting(request):
    return render(request, 'setting.html')
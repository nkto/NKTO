from django.shortcuts import render

def hello(request):
    context = {}
    context['rlt'] = 'hello world~~~'
    return render(request, 'hello.html', {'hello':'asdfas'})
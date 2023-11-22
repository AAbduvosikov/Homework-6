from django.shortcuts import render

def myview(request):
    return render(request=request, template_name='main.html',context={})
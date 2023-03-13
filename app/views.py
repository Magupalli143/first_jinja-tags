from django.shortcuts import render

# Create your views here.
def first_jinja(request):
    d={'name':'suresh','age':22}
    return render(request,'first_jinja.html',context=d)
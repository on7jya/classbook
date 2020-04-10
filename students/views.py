from django.shortcuts import render


def homepage_view(request):
    return render(request=request, template_name="main/home.html")

from django.shortcuts import render, HttpResponse

html_base = """

<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca De</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""


# Create your views here.
def home(request):
    return HttpResponse(html_base + "<h2>Portada</h2>")


def about(request):
    return HttpResponse(html_base + "<h2>Acerca de</h2>")


def portfolio(request):
    return HttpResponse(html_base + "<h2>Portafolio</h2>")


def contact(request):
    return HttpResponse(html_base + "<h2>Contacto</h2>")

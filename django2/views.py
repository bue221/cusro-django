from django.shortcuts import render, HttpResponse, redirect
from django2.models import Articulo, Categoria
from django2.forms import FormArticulo
from django.contrib import messages

# Create your views here.

#MVC =  Modelo Vista Controlador
#MVT =  Modelo Vista Template

#variable
lenguajes = ['javascript','C','python']

def inicio(request):
    return render(request, 'index.html', {
        'buena': 'buena',
        'lenguajes': lenguajes
        })


def contacto(request,nombre=""):
    return render(request, 'contact.html')


def save(request):
    return render(request, 'create.html')


def create(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
    
        articulo = Articulo(
                title = title,
                content = content,
                public = public
                )
        articulo.save()
        return HttpResponse("Su articulo ya esta publicado")

    else:
        return HttpResponse("No se ha creado el articulo")

def create_articulo(request):

    if request.method == 'POST':

        formulario = FormArticulo(request.POST)

        if formulario.is_valid():

            datos_form = formulario.cleaned_data

            title = datos_form.get('title')
            content = datos_form['content']
            public = datos_form['public']

            articulo = Articulo(
                title = title,
                content = content,
                public = public
                )
            articulo.save()

            #crear mensaje flash
            messages.success(request, f"Exito en la creacion del articulo {articulo.id}")

            return redirect('articulos')
    else:
        formulario = FormArticulo()

    return render(request, 'create-class.html',{
        'form': formulario
        })


def articulo(request,num):

    articulo = Articulo.objects.get(pk=num)

    if articulo.public:
        html = f'esta publicado {articulo.title}'
    else:
        html = f'NO esta publicado {articulo.public}'

    return HttpResponse(html);

def editar(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.title = 'comida'
    articulo.save()

def articulos(request):

    articulo = Articulo.objects.order_by('id')

    return render(request, 'articulo.html', {
        'articulo': articulo
        })

    return HttpResponse('')

def borrar(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')

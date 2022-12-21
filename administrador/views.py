from django.shortcuts import render
from store.models import Product
from category.models import Category
from msilib.schema import Error
from . models import Reporteria
from accounts.models import Account
# Create your views here.

def inicio(request):
    return render(request, 'administrador/inicio.html')    


def verFormulario(request):
    return render(request, 'administrador/crear.html')

def verform_categoria(request):
    return render(request, 'administrador/crear_categoria.html')    

def crear_categoria(request):

    category_name = request.POST['category_name']
    slug = request.POST['slug']
    
     
    try:
        Category.objects.create(
                category_name = category_name,
                slug = slug
                )
    
    except Exception as ex:
        """if str(ex.__cause__).find('administrador_product.product_name') > 0:
            print('Ha ocurrido un problema al registrar el artículo, número de articulo ya a sido ingresado.')

        elif str(ex.__cause__).find('administrador_product.description') > 0:
            print('Ha ocurrido un problema al registrar el artículo, el nombre del articulo no debe estar vacío.')

        elif str(ex.__cause__).find('administrador_product.price') > 0:
            print('Ha ocurrido un problema al registrar el artículo, el stock no debe estar vacío.')

        elif str(ex.__cause__).find('administrador_product.image') > 0:
            print('Ha ocurrido un problema al registrar el artículo, el campo de ubicación no debe estar vacío')

        elif str(ex.__cause__).find('administrador_product.category') > 0:
            print('Ha ocurrido un problema al registrar el artículo, el camop de descripción no debe estar vacío'  ) 

        else:
            print('Ha ocurrido un problema al registrar el articulo.')"""
        
        print('se ha ingresado el articulo con exito')
    return render(request, 'administrador/crear_categoria.html')


def crear_producto(request):
    
    product_name = request.POST['product_name']
    slug = request.POST['slug']
    description = request.POST['description']
    price = request.POST['price']
    image = request.POST['image']
    category = request.POST['category']
    stock = request.POST['stock']
    create_date = request.POST['create_date']

    category = Category.objects.get(category_name=category) 
    print(category)
    Product.objects.create(
        product_name = product_name,
        slug = slug,
        description = description, 
        price = price,
        image = image, 
        category = category,
        stock = stock,
        create_date = create_date, 
                
                )

    #username = Account.objects.get(account=username)
    Reporteria.objects.create(
      username = 'bayronmorales22@hotmail.com',  
      accion = "crear", 
      product_name = product_name,
      slug = slug,
      stock = stock,   
    )
        
    print('se ha ingresado el articulo con exito')

    return render(request,'administrador/inicio.html')


def lista(request):
    productos = Product.objects.all()
    print(productos)
    return render(request,'administrador/lista_productos.html', {'productos':productos})


def categories(request):
    categories = Category.objects.all().filter(is_available=True)
    print(categories) 
    return render(request, 'administrador/lista_productos.html', {'categories':categories})



def eliminar_producto(request, product_name):
  
    try:
        productos = Product.objects.get(product_name = product_name)
        
        slug = Product.objects.get(slug = slug)
        print(product_name)
        stock = Product.objects.get(stock = stock)
        print(slug)
        Reporteria.objects.create(
        username = 'bayronmorales22@hotmail.com',  
        accion = "eliminar", 
        product_name = product_name,
        slug = slug,
        stock = stock
        )
        productos.delete()
        print("El Articulo ha sido eliminado exitosamente.")
        return render(request,"administrador/lista_productos.html")

    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            print( 'No se ha encontrado un articulo  asociado. Por favor, vuelva a intentarlo.')
        else:
            print( 'Ha ocurrido un problema al eliminar el articulo.')
        
        return render(request,"administrador/lista_productos.html")




def editar_productos(request, product_name):
    try:
        productos = Product.objects.get(product_name = product_name)
        return render(request, "administrador/editar_producto.html", { "prod":productos})
        
    except:
        productos = None

    if productos == None:
        try:
             
            product_name = request.POST["product_name"]
            productos = Product.objects.get(product_name = product_name)
        except:
            product_name = None
    
        if product_name != None:
            
            product_name = request.POST['product_name']
            slug = request.POST['slug']
            description = request.POST['description']
            price = request.POST['price']
            image = request.POST['image']
            category = request.POST['category']
            stock = request.POST['stock']
            create_date = request.POST['create_date'] 
            category = Category.objects.get(category_name=category) 
            
            productos.product_name = product_name
            productos.slug = slug
            productos.description = description
            productos.price = price
            productos.category = category
            productos.image = image
            productos.stock = stock
            productos.create_date = create_date

            try:
                productos.save()
                Reporteria.objects.create(
                username = 'bayronmorales22@hotmail.com',  
                accion = "Editar", 
                product_name = product_name,
                slug = slug,
                stock = stock,   
                )

                print("Se ha actualizado el Articulo")
            except:
                print("Se ha ocurrido un error al actualizar el Articulo")

            return render(request, "administrador/lista_productos.html")
        
        else:
            print(productos)
            print("No se ha encontrado el Articulo")
            return render(request, "administrador/lista_productos.html")
    else:
        print("No se encontró el Articulo solicitado")
        return render(request, "administrador/lista_productos.html")         